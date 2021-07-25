
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials


from flask import Flask, request

from flask_ngrok import run_with_ngrok
  
app = Flask(__name__)

cred = credentials.Certificate("paul-portfolio-6aec1-firebase-adminsdk-niw9v-2d48e175b1.json")



@app.route("/", methods=['POST','GET'])
def hello():
    content = request.json
    data = content['event']['data']['new']
    



    # This registration token comes from the client FCM SDKs.
    registration_token = 'fhbsmspAQtqjQr7gyYurSD:APA91bFJfzb1P1p9ngzI26NhWVs_jdW_3H0FQevetgLajxf34ggewX5wojUuTnQQgWRhSuOneYSX9huMmBx_NJjUMgSAqrm3Q3OplU9X5WRGXMBBVXvZmmrw33J7jNTl7bwGC2sYDn1z'

    # See documentation on defining a message payload.
    message = messaging.Message(
            notification=messaging.Notification(
            title="New Message in Portfolio",
            body=data['full_name']+" sent you a message titled "+data['subject']
    ),
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    return 'Successfully sent message:' + response

  
if __name__ == "__main__":
    firebase_admin.initialize_app(cred)
    app.run()