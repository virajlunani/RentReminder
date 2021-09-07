from twilio.rest import Client
import os

def lambda_handler(event, context):
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    tenant_1 = os.environ['TENANT_1']
    tenant_2 = os.environ['TENANT_2']
    my_twilio = os.environ['MY_TWILIO']

    client = Client(account_sid, auth_token)

    body = 'Pay Rent. Please venmo $550 to @Viraj-Lunani. Thanks.'

    message_1 = client.messages.create(to=tenant_1, from_=my_twilio, body=body)
    message_2 = client.messages.create(to=tenant_2, from_=my_twilio, body=body)
