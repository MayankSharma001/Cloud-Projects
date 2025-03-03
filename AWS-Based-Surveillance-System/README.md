# AWS-Based AI-Powered Security Surveillance System

## Introduction

This documentation provides a step-by-step guide to setting up an AWS-based security surveillance system that captures images from a webcam
detects humans using OpenCV, stores images in an S3 bucket, and triggers an AWS Lambda function to send notifications using AWS SNS.

## Prerequisites

Before getting started, ensure you have the following:

  - AWS Account

  - AWS CLI Installed & Configured

  - Python Installed (3.x recommended)

  - Boto3 and OpenCV Installed

  - AWS IAM Role with Required Permissions

### Step 1: Install AWS CLI & Configure

1. Download and install AWS CLI from AWS CLI official page.

2. Configure AWS CLI:
    - aws configure
    - Enter your AWS Access Key, Secret Key, Region, and Output format.
      
### Step 2: Install Required Python Packages
    - pip install boto3 opencv-python ultralytics

### Step 3: Create an S3 Bucket
1. Go to AWS S3 in the AWS Console.
2. Click Create Bucket.
3. Enter a unique bucket name (e.g., mayank-security-bucket).
4. Select a region and configure permissions as needed.
5. Click Create Bucket.

### Step 4: Set Up an AWS SNS Topic
1. Go to AWS SNS in the AWS Console.
2. Click Create Topic.
3. Select Standard type and name it human-detection-alert.
4. Copy the Topic ARN for later use.
5. Create a subscription to receive email alerts:
6. Click Create Subscription.
7. Choose the Topic you just created.
8. Select Email as the protocol.
9. Enter your email address and confirm the subscription from your email inbox.

### Step 5: Create an IAM Role for Lambda
1. Go to AWS IAM → Roles → Create Role.
2. Select Lambda as the trusted entity.
3. Attach these policies:
      - AmazonS3FullAccess
      - AmazonSNSFullAccess
      - AWSLambdaBasicExecutionRole
4. Name the role lambda-human-detection-role and create it.

### Step 6: Create an AWS Lambda Function
1. Go to AWS Lambda → Create Function → Choose "Author from scratch".
2. Set a name (e.g., HumanDetectionLambda).
3. Choose Python 3.x as the runtime.
4. Attach the IAM role created earlier.
5. Add an S3 trigger:
6. Click Add Trigger.
7. Select S3.
8. Choose your bucket.
9. Select event type as PUT.
10. Click Add.

### Step 7: Set Up Local Machine for Human Detection

### Step 8: Testing the System
1. Run the Python script locally.
2. Verify that images are uploaded to S3 when a human is detected.
3. Check if AWS Lambda is triggered.
4. Confirm that SNS notifications are received.
