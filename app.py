# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify, request, render_template
# fbchat
from fbchat import Client
from fbchat.models import *
import time

app = Flask(__name__)


email	 = "user@email.com"
password = "hereyourpassword!"


# keep session
client 	= Client(email, password) 
session_cookies = client.getSession()



@app.route('/facebook/user/send', methods=['GET']) 
def send_message():

    contact      = request.args.get('contact', default = '', type = str)
    message  	 = request.args.get('message', default = '', type = str)
 
    print(contact,message)
    ok  = False

    
    try:
		client.setSession(session_cookies)
		friend = client.searchForUsers(contact, limit=1)  

		UID = friend[0].uid
		print('UID :',UID)
		#friend  = friends[0] 
		sent	= client.send(Message(text=message),thread_id=UID, thread_type=ThreadType.USER)
		ok  	= True

    except Exception as e:
        print(e)
    print(ok)
    return jsonify(ok)




if __name__ == '__main__':
	app.run(debug=False) # host='0.0.0.0',port='5050'
