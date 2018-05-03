import os
from flask import Flask, request, redirect

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/sms", methods = ["GET", "POST"])
def sms_reply():
    try:
        number = request.form["From"]
        message_body = request.form["Body"]
        resp=MessagingResponse()
        resp.message("Hello {}, you said: {}".format(number, message_body))
        # print("request.form is", request.form)
    except:
        resp = "hello"

    return str(resp)

if __name__ == "__main__":
    app.run()
