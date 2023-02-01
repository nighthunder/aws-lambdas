import json
import boto3
import requests
import os
from re import sub
import unicodedata
import re
import awswrangler as wr
import pandas as pd

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
            excel_data = pd.Dataframe(pd.read_excel(data.content));
        
        wr.s3.to_parquet(excel_data, "s3://mitre-datalake-raw/anapro/api/view_vw_analisecredito_v1/vw_analisecredito_v1.parquet")
        
        print("Resource " + str(urlget)+" sucessfully created!")
        
    except Exception as e:
        print("Ocorreu um erro ao chamar a API " + str(urlget) +": "+ str(e))
            
    
    
   
    
    
    

