import json
import boto3
import os

def lambda_handler(event, context):
    
    client_dms = boto3.client('dms') 
    arn_evt_bridge_dms_oracle = os.environ['ARN_DMS_TASK_ORACLE_TABLES']
    arn_evt_bridge_dms_mysql_tables = os.environ['ARN_DMS_TASK_MYSQL_TABLES']
    arn_evt_bridge_dms_mysql_views = os.environ['ARN_DMS_TASK_MYSQL_VIEWS']
    
    try:
        
        # ORACLE
        #response = client_dms.start_replication_task(
        #ReplicationTaskArn= arn_evt_bridge_dms_oracle,
        #StartReplicationTaskType= 'reload-target')
        print("Oracle Mega database extraction EventBridge DMS started successfuly!")
        
        
        # MYSQL TABLES
        response = client_dms.start_replication_task(
        ReplicationTaskArn=arn_evt_bridge_dms_mysql_tables,
        StartReplicationTaskType= 'reload-target')
        print("Mysql tables Hypnobox database extraction EventBridge DMS started successfuly!")
        
        
        
        # MYSQL VIEWS
        response = client_dms.start_replication_task(
        ReplicationTaskArn=arn_evt_bridge_dms_mysql_views,
        StartReplicationTaskType= 'reload-target')
        print("Mysql database GesCorp extraction EventBridge DMS started successfuly!")
        
        
    except Exception as e:
        print("Ocorreu um erro ao chamar o EventBridge:" + str(e))
        

    
    
    
   