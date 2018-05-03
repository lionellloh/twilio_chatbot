from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc8dc34c90e61bacedaaa375638064502"
# Your Auth Token from twilio.com/console
auth_token  = "a765a30b6165c7d2f1e7f4660cc36f8f"




client = Client(account_sid, auth_token)

call = client.calls.create(
                        url="http://demo.twilio.com/docs/voice.xml",
                        from_="+12763788148",
                        to="+65 97895918"
                    )

print(call.sid)
# message = client.messages.create(
#     to="+6597895918",
#     from_="+12763788148 ",
#     body="Hello from Python!")
#

# The following block of code serves to check for the latest message.
# while True:
#     messages = []
#     for sms in client.messages.list():
#         if sms.direction == "inbound":
#             messages.append((sms.body))
#     x = len(messages)
#     while x == len(messages):
#         messages = []
#         for sms in client.messages.list():
#             if sms.direction == "inbound":
#                 messages.append((sms.body))
#         # print("The last message is {}".format(messages[0]))
#     print("The new message is {}".format(messages[0]))


client = Client(account_sid, auth_token)

call = client.calls.create(
                        url="http://demo.twilio.com/docs/voice.xml",
                        from_="+12763788148",
                        to="+65 97895918"
                    )

print(call.sid)

# Make it check every one sec
#TODO: Make the SMS checking function more elegant
#TODO: Show last 5 messages for Aaron. Perhaps can try a list of dictionaries
#TODO: Make the sending text a function
#TODO: Put the thing on flask - Make a help guide for him
# print(message.sid)


