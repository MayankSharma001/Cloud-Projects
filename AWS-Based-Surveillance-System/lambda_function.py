import boto3
import json
import datetime


s3 = boto3.client("s3")
sns = boto3.client("sns")


SNS_TOPIC_ARN = "sns arn"

def lambda_handler(event, context):
    #S3 Event Details
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    
    print(f"New image uploaded: {image_name} in bucket: {bucket_name}")

    timestamp = datetime.datetime.now().strftime("Date-%d-%m-%Y_Time-%H-%M-%S")
    print("🚨 Human Detected! Sending SNS Notification...")

    #Send SNS Alert
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=f"🚨 Alert! Human detected at {timestamp}. Image saved in S3: {image_name}",
        Subject="Security Alert!",
    )

    print("✅ SNS Notification Sent!")
    
    return {
        "statusCode": 200,
        "body": json.dumps("Processing Done!")
    }
