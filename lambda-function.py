import json
import boto3
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

S3_BUCKET_NAME = 't2s-form-submissions'
DYNAMODB_TABLE_NAME = 'T2SFormSubmissions'

def lambda_handler(event, context):
    body = json.loads(event['body'])

    first_name = body['first_name']
    phone_number = body['phone_number']
    message = body['message']
    submission_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    # Store data in DynamoDB
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    table.put_item(
        Item={
            'submission_id': submission_id,
            'first_name': first_name,
            'phone_number': phone_number,
            'message': message,
            'timestamp': timestamp
        }
    )

    # Store data in S3
    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=f'submissions/{submission_id}.json',
        Body=json.dumps(body),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Submission successful'})
    }
