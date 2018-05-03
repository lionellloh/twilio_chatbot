"""Edit the body data to simulate sending an SMS"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://237ef39e.ngrok.io/sms' # Set destination URL here
var = ([('ToCountry', 'US'), ('ToState', 'VA'), ('SmsMessageSid', 'SM15ddfef9992e0be42dac31ae513c46dc'), ('NumMedia', '0'), ('ToCity', 'WYTHEVILLE'), ('FromZip', ''), ('SmsSid', 'SM15ddfef9992e0be42dac31ae513c46dc'), ('FromState', ''), ('SmsStatus', 'received'), ('FromCity', ''), ('Body', 'Happy'), ('FromCountry', 'SG'), ('To', '+12763788148'), ('ToZip', '24382'), ('NumSegments', '1'), ('MessageSid', 'SM15ddfef9992e0be42dac31ae513c46dc'), ('AccountSid', 'ACc8dc34c90e61bacedaaa375638064502'), ('From', '+6597895918'), ('ApiVersion', '2010-04-01')])
post_fields = var     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()

print(json)
