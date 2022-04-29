import boto3
import ast

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

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

#print(type(message))

for i in message:
    if i == 'Body':
       tostr = str([message[i]])
       print(type(tostr))
       tolist = ast.literal_eval(tostr)
       for y in tolist:
           print(type(y))

#print(receipt_handle)

# ["Round3", {"computer1_choice": 2, "computer2_choice": 1, "Won": "Computer1", "Lost": "Computer2", "Tie": "False"}]