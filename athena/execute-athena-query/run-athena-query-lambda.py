import boto3
import pandas as pd
import io
import re
import time


def athena_query(client, params):
    
    response = client.start_query_execution(
        QueryString=params["query"],
        QueryExecutionContext={
            'Database': params['database']
        },
        ResultConfiguration={
            'OutputLocation': 's3://' + params['bucket'] + '/' + params['path']
        }
    )
    return response
    
    
def athena_to_s3(session, params, max_execution = 5):
    client = session.client('athena', region_name=params["region"])
    execution = athena_query(client, params)
    execution_id = execution['QueryExecutionId']
    state = 'RUNNING'

    while (max_execution > 0 and state in ['RUNNING', 'QUEUED']):
        max_execution = max_execution - 1
        response = client.get_query_execution(QueryExecutionId = execution_id)

        if 'QueryExecution' in response and \
                'Status' in response['QueryExecution'] and \
                'State' in response['QueryExecution']['Status']:
            state = response['QueryExecution']['Status']['State']
            if state == 'FAILED':
                return False
            elif state == 'SUCCEEDED':
                s3_path = response['QueryExecution']['ResultConfiguration']['OutputLocation']
                filename = re.findall('.*\/(.*)', s3_path)[0]
                return filename
        time.sleep(1)
    
    return False
    
def lambda_handler(event, context):

    params = {
        'region': 'us-east-1',
        'database': 'parquet_test_files',
        'bucket': 'athena-us-east-1-configuration',
        'path': 'temp/athena/output',
        'query': 'SELECT * FROM user LIMIT 100'
    }

    session = boto3.Session()
    
    # Query Athena and get the s3 filename as a result
    s3_filename = athena_to_s3(session, params)

    print(s3_filename)