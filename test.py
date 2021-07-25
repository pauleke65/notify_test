
import firebase_admin
from firebase_admin import messaging
default_app = firebase_admin.initialize_app()


# This registration token comes from the client FCM SDKs.
registration_token = 'eK6n_cANQW6vlkp79z1ffs:APA91bG8vAAX-h_8hTIdauUIWG82wHQpl7fax6r57MeyBkzq4uxSSyNyZTMnkkrI2xsr2AroMRN9UmrqVSIzaZuEiHpwewIIggPlxLJfMjHDgEa6UkSnryAJfU311jfriOrUSMjgE0ec'

# See documentation on defining a message payload.
message = messaging.Message(
        notification=messaging.Notification(
        title="FCM Message",
        body="This is an FCM notification message!"
),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)

# import requests
# from requests.structures import CaseInsensitiveDict

# url = "https://fcm.googleapis.com/v1/projects/paul-portfolio-6aec1/messages:send"

# headers = CaseInsensitiveDict()
# headers["Authorization"] = "Bearer  AAAALXxhD2Q:APA91bF5-IGRIUg7yFLtlkaQ9rgcY3HBfzojxAC11JCH53CH2Dk-LHMw3AbRWmeTwgWPf67PF8P_i94mmG4nU8R-xZfXp0rQROLdiNhHge9P_Fj1EluK0fXSyhu-GClD7Vu-TToinX5A"
# headers["Content-Type"] = "application/json"

# data = """
# {
#    "message":{
#       "token":"eK6n_cANQW6vlkp79z1ffs:APA91bG8vAAX-h_8hTIdauUIWG82wHQpl7fax6r57MeyBkzq4uxSSyNyZTMnkkrI2xsr2AroMRN9UmrqVSIzaZuEiHpwewIIggPlxLJfMjHDgEa6UkSnryAJfU311jfriOrUSMjgE0ec",
#       "notification":{
#         "body":"This is an FCM notification message!",
#         "title":"FCM Message"
#       }
#    }
# }

# """


# resp = requests.post(url, headers=headers, data=data)

# print(resp.status_code)

