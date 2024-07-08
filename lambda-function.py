import json
import boto3
import uuid

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('T2SFormSubmissions')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        submission_id = str(uuid.uuid4())
        first_name = body['first_name']
        phone_number = body['phone_number']
        message = body['message']
        
        # Save to S3
        s3_client.put_object(
            Bucket='t2s-form-submissions',
            Key=f'submission_{submission_id}.json',
            Body=json.dumps(body)
        )
        
        # Save to DynamoDB
        table.put_item(
            Item={
                'submission_id': submission_id,
                'first_name': first_name,
                'phone_number': phone_number,
                'message': message
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'message': 'Submission successful'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': str(e)})
        }
