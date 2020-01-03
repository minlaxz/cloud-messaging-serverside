import requests
from firebase_admin import db
from firebase import firebase_cred
import json
url = "https://fcm.googleapis.com/fcm/send"

def sender(clientToken):
    print(clientToken)
    payload = {
      "notification":{
      "title": "Car Map Notification",
      "body": "(Server Generated this message to all cross-devices.)",
      "icon": "firebase-logo.png",
      "click_action": "https://laxz-test.firebaseapp.com"},
      "to":clientToken
    }

    headers = {
      'Authorization': 'key=AAAA2xz4m8E:APA91bE1yj9mIZgSd12sclR5W_Q9TUwCZm3YuPiCXA_N4cECzgNZToTsVkpgZQYo8zIeXbWKXqD34u62GQFsZ7pKfepEecyzR11G8giyCeqc-6JXd6d6FdTOteDmFvbxC7Q5xraEvi-B',
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))


tokens = db.reference('tokens').get()
for key in tokens:
    i = tokens[key]['token']
    sender(i)