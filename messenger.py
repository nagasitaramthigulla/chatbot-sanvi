from requests import post
from api_key import PAGE_TOKEN

def send_message(recepient,message):
    url='https://graph.facebook.com/v2.6/me/messages?access_token='+PAGE_TOKEN
    r=post(url,json={  "notification_type":"REGULAR"  ,  "messaging_type": "RESPONSE",   "recipient":{    "id":recepient  },  "message":{    "text":message  }  },headers={})
    print(r.json())