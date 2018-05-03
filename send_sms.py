from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9ea6a05336f1559b64eeeb3a6b324d92"
# Your Auth Token from twilio.com/console
auth_token  = "d4cc3d11965d321af0365acbe2fe8937"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="82238302",
    from_="+6582410049",
    body="Hello from Python!")
#
# print(message.sid)

for sms in client.messages.list():
    print(sms.to)
