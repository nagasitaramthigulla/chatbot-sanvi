# Generates a bot response from a user message
import random
from wiki import wikisearch
import json
from requests import get
from urllib3.poolmanager import PoolManager as pm
from api_key import PAGE_TOKEN

greetings=["hi","hello","hey","namaste","yo","hii"]
replygreet=["Hi.","Hello.","Namaste.","Greetings."]

def generateReply(message,**kwargs):
    tokens=message.split()
    if 'nlp' in kwargs:
        nlp=kwargs['nlp']['entities']
        if 'greetings' in nlp and nlp['greetings'][0]['confidence']>0.85:
            url='https://graph.facebook.com/v2.12/'+kwargs['id']+'?access_token='+PAGE_TOKEN
            s=json.loads(pm().request('GET',url).data.decode())
            return random.choice(replygreet)+' '+s.get('first_name',' ')


        if tokens[0].lower()=="wiki":

            
            if len(tokens)>1 and tokens[0].lower()=="wiki":
                return wikisearch(str(tokens[1:]))


            else:
                return "wiki [your keyword]"
        
    return "I don't understand." # Otherwise the bot doesn't understand what the user said