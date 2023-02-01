#Lambda para fazer uma chamada autenticada numa api que retorna um XLXS e converte # para CSV e salva em um bucket no S3:

import json
import boto3
import requests
import openpyxl
import pandas as pd
import os

file_extension = "xlsx"

def lambda_handler(event, context):
   
    try:
        s3 = boto3.resource('s3')
        bucket = os.environ['NOME_BUCKET']
        anapro_username = os.environ['ANAPRO_USERNAME'] 
        anapro_passwd = os.environ['ANAPRO_PASSWD']
        urlget = os.environ['URL_GET_API']
            
        data = requests.get(urlget, auth=(anapro_username, anapro_passwd))
        
        if file_extension == 'xlsx':
            excel_data = pd.read_excel(data.content, engine='openpyxl')
        elif file_extension == 'xls':
            excel_data = pd.read_excel(data.content)
            
        csvData = excel_data.to_csv(sep=";", index=False);
        
        s3object = s3.Object(bucket, os.environ['NOME_OBJETO'])
        s3object.put(
            Body=csvData
        )
        
        print("Resource " + str(urlget)+" sucessfully created!")
        
    except Exception as e:
        print("Ocorreu um erro ao chamar a API " + str(urlget) +": "+ str(e))
            
    
    
   
    
    
    

