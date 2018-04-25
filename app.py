import os, sys
from flask import Flask, request
from pymessenger import Bot
from generate_reply import generateReply
from messenger import send_message
#page access token
#bot=Bot(PAGE_TOKEN)

app=Flask(__name__)
@app.route('/',methods=['GET'])
def verify():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch",403
        print(request.args["hub.challenge"],200)
        return request.args["hub.challenge"],200
    return "Hi",200


@app.route('/',methods=['POST'])
def webhook():
    data=request.get_json()
    log(data)

    if data['object']=='page':
        for entry in data['entry']:
            for messagingEvent in entry['messaging']:
                senderId=messagingEvent['sender']['id']
                if messagingEvent.get('message'):
                    if 'text' in messagingEvent['message']:
                        messageText=messagingEvent['message']['text']
                        if 'nlp' in messagingEvent['message'] and len(messagingEvent['message']['nlp'])>0 :
                            response=generateReply(messageText,id=senderId,nlp=messagingEvent['message']['nlp'])
                        else: 
                            response=generateReply(messageText,id=senderId)
                        send_message(senderId,response)
    return "ok",200


def log(str):
    print(str)
    sys.stdout.flush()


if __name__=="__main__":
    app.run(debug=True,port=90)

