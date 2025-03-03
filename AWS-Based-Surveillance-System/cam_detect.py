import cv2
import boto3
import datetime


s3 = boto3.client("s3")
sns = boto3.client("sns")

#AWS Configurations
BUCKET_NAME = "bucket name"
SNS_TOPIC_ARN = "sns arn"

#Load Haarcascade for human detection (Try different cascades)
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")

#OpenCV Video Capture
cap = cv2.VideoCapture(0)  #0 is for default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Convert frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)

    #Draw rectangles for detected humans
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    #Save the image locally
    timestamp = datetime.datetime.now().strftime("Date-%d-%m-%Y_Time-%H-%M-%S")
    image_path = f"captured_{timestamp}.jpg"
    cv2.imwrite(image_path, frame)

    #Upload the image to S3 bucket
    s3.upload_file(image_path, BUCKET_NAME, image_path)

    #If human is detected, send SNS notification
    if len(humans) > 0:
        print("Human Detected! Sending SNS Notification")
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"Human detected at {timestamp}. Image saved in S3: {image_path}",
            Subject="Security Alert!",
        )

    #Show the Frame
    cv2.imshow("Live Stream", frame)

    #Exit on pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
