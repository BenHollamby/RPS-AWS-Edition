import mysql.connector
import boto3
import json

client = boto3.client('secretsmanager')

response = client.get_secret_value(
    SecretId='RPS-DB-Creds'
)

database_secrets = json.loads(response['SecretString'])

try:
    connection = mysql.connector.connect(host='rps-database-mysql-01.c9egdgsuh48o.ap-southeast-2.rds.amazonaws.com',
                                         database='rps-database-mysql-01',
                                         user='admin',
                                         password=database_secrets['RPS-MySQL-DB-Creds'])

    mySql_Create_Table_Query = """CREATE TABLE Games ( 
                             Round varchar(250) NOT NULL,
                             'Computer 1' varchar(250) NOT NULL,
                             'Computer 2' varchar(250) NOT NULL,
                             Won int,
                             Lost int,
                             Tie int """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("RPS Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")