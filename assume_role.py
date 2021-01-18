# used for ApiGateway IAM_AUTH API
# sudo pip install aws-requests-auth boto3
# sudo pip install --upgrade awscli
import boto3
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
session = boto3.Session()

sts_client = boto3.client('sts')

assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::1234567890:role/<role_name>",
    RoleSessionName="AssumeRoleSession1"
)

# From the response that contains the assumed role, get the temporary
# credentials that can be used to make subsequent API calls
credentials = assumed_role_object['Credentials']

auth = AWSRequestsAuth(
                    aws_access_key=credentials['AccessKeyId'],
                    aws_secret_access_key=credentials['SecretAccessKey'],
                    aws_token=credentials['SessionToken'],
                    aws_host='api.example.com',
                    aws_region='<aws_region>',
                    aws_service='execute-api')
response = requests.get(
    url='https://api.example.com/api/v1/get_stuff',
    params={
        "user_ids": ["<user_id>"]
    },
    auth=auth
)

print(credentials['AccessKeyId'])
print(credentials['SecretAccessKey'])
print(credentials['SessionToken'])

print(response.content)
print(response.status_code)

