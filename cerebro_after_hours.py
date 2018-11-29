import csv
import boto3
import os
import requests
#S3 resource
s3 = boto3.client('s3')
Bucket = "cerebro-bucket01"
Key = "resources (1).csv"
raw_file = s3.get_object(Bucket=Bucket, Key=Key) #get the file from s3 bucket raw content
#print(raw_file)
file = raw_file['Body'].read().decode('utf-8').splitlines(True) #read the body of the required content
# print(file)
input_file = csv.DictReader(file)

def ec2_instance(input_file): #a method
    for row in input_file:
        if 'EC2 Instance' in row['Resource type']:
            print(row['ID'])

 request.post(os.getenv('CEREBROURL'),ec2_id=ec2_instance(input_file))
