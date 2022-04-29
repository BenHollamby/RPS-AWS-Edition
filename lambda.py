import boto3

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

print(type(message))

for i in message:
    if i == 'Body':
        print(message[i])

#print(receipt_handle)

#["Round3", {"computer1_choice": 2, "computer2_choice": 1, "Won": "Computer1", "Lost": "Computer2", "Tie": "False"}]