import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    rekognition = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = "imagerecognitionbucketrageeb", Key ="bernie.jpg" )
    file_content = fileObj["Body"].read()
    response = rekognition.detect_labels(Image = { "S3Object" : {"Bucket" : "imagerecognitionbucketrageeb", "Name" : "bernie.jpg" }}, MaxLabels=3, MinConfidence=70 )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }