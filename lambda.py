import boto3
import json

sqs = boto3.client('sqs')
queue_url = 'https://sqs.ap-southeast-2.amazonaws.com/291505762885/RPS-SQS'

response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = json.loads(response['Messages'][0]['Body'])
print(message)
round = message[0]
results = message[1]

print(round)
for result in results:
    print(result, results[result])