import json
import boto3
import os

s3_client = boto3.client("s3")
dynamodb_client = boto3.client("dynamodb")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
TABLE_NAME = os.environ.get("TABLE_NAME")

def lambda_handler(event, context):
    # Write to DynamoDB
    dynamodb_client.put_item(
        TableName=TABLE_NAME,
        Item={"id": {"S": "1"}, "message": {"S": "Hello from Lambda!"}}
    )
    
    # Write to S3
    s3_client.put_object(Bucket=BUCKET_NAME, Key="hello.txt", Body="Hello from Lambda!")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Lambda executed successfully"}),
        "headers": {"Content-Type": "application/json"}
    }
