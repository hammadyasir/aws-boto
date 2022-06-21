import boto3
# low level api connect with aws
s3_client = boto3.client('s3')
print("My client are",s3_client)


# To connect to the high-level interface, you’ll follow a similar approach, but use resource():