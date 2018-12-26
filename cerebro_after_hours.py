import csv
import boto3
import os
import requests
#S3 resource
def lambda_handler(event, context): 
    s3 = boto3.client('s3')
    Bucket = event['Records'][0]['s3']['bucket']['name']
    Key  = event['Records'][0]['s3']['object']['key']
    raw_file = s3.get_object(Bucket=Bucket, Key=Key)
    file = raw_file['Body'].read().decode('utf-8').splitlines(True) 
    print(file)
input_file = csv.DictReader(file)

def ec2_instance(input_file): #a method
    for row in input_file:
        if 'EC2 Instance' in row['Resource type']:
            print(row['ID'])

 requests.post(os.getenv('CEREBROURL'),ec2_id=ec2_instance(input_file))
