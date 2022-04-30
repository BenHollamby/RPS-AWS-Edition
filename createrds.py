import boto3
import json

client = boto3.client('secretsmanager')

response = client.get_secret_value(
    SecretId='RPS-DB-Creds'
)

database_secrets = json.loads(response['SecretString'])
#print(database_secrets['RPS-MySQL-DB-Creds'])

client = boto3.client('rds')

response = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='RPS-database-MySQL-01',
    Engine='MySQL',
    MasterUserPassword=database_secrets['RPS-MySQL-DB-Creds'],
    MasterUsername='admin',
)

print(response)