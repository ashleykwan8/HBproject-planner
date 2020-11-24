from secrets import ACCOUNT_SID, AUTH_TOKEN, NUMBER
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Hello There!",
                     from_='+17155977935',
                     to=NUMBER
                 )

print(message.sid)