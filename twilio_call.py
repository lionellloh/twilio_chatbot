"""
Usage:
Use this to call - put twilio_call.py in the same folder as your Kivy App

from twilio_call import *

call()
"""

from twilio.rest import Client


def call():
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

    return (call.sid)
