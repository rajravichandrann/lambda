import boto3
import botocore
import json
import os
import psycopg2
import db_config #DB connect details in db_config.py


#connect to RDS
dbname = db_config.db_name
user = db_config.db_username
host =


#s3 client connection session
#bucketname and key are retrived from the event.
client = boto3.resource('s3')
