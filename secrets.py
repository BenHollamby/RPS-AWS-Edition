import boto3
import json

client = boto3.client('secretsmanager')

response = client.get_secret_value(
    SecretId='RPS-DB-Creds'
)

database_secrets = json.loads(response['SecretString'])
print(database_secrets['RPS-MySQL-DB-Creds'])