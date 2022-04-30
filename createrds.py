import boto3
import json

secret = boto3.client('secretsmanager')

response = secret.get_secret_value(
    SecretId='RPS-DB-Creds'
)

database_secrets = json.loads(response['SecretString'])
rds = boto3.client('rds')

response = rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='RPS-database-MySQL-02',
    Engine='MySQL',
    MasterUserPassword=database_secrets['RPS-MySQL-DB-Creds'],
    MasterUsername='admin',
    MultiAZ=True
)

DBInstanceIdentifier='RPS-database-MySQL-02'

response = rds.describe_db_instances(DBInstanceIdentifier=DBInstanceIdentifier)

while True:
    response = rds.describe_db_instances(DBInstanceIdentifier=DBInstanceIdentifier)
    status = response['DBInstances'][0]['DBInstanceStatus']
    if status != 'available':
        continue
    else:
        break

address = response.get('DBInstances')[0].get('Endpoint').get('Address')
print(address)