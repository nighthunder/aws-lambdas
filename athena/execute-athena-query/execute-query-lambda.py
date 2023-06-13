import json
import boto3
import time

def lambda_handler(event, context):

    my_query = "SELECT * FROM user_data"
    database_name = 'parquet_test_files'

    athena_client = boto3.client('athena')

    QueryResponse = athena_client.start_query_execution(
        QueryString = my_query,
        QueryExecutionContext={
            'Database': database_name
        },
        ResultConfiguration={
            'OutputLocation': 's3://athena-us-east-1-configuration/'
        }
    )

    print(QueryResponse)

    QueryID = QueryResponse['QueryExecutionId']

    time.sleep(15)

    query_results = athena_client.get_query_results(QueryExecutionId = QueryID)

    for row in query_results['ResultSet']['Rows']:
        print(row)