import ssl
from datetime import datetime
from time import sleep

import certifi
import RPi.GPIO as GPIO
import slack_sdk as slack
from picamera import PiCamera

SLACK_BOT_TOKEN='xoxb-367476445521-5570460785970-7lV4pRVodQOoqlTdPTnGGE1o'
SLACK_SIGNING_SECRET='b6959abc7459745a7f9b0839a93999a5'
SLACK_APP_CHANNEL='C05GBQUKUF9' # 'CRREV5C9L'

CHANNEL = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.IN)

camera = PiCamera()
camera.rotation = 180

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context)
auth_test = client.auth_test()

timer=datetime.now()
counter=0

print(f'Starting: {auth_test["user"]} - {auth_test["user_id"]}')

def getDelta(now: datetime):
    return (now-timer).seconds

def takePicture():
    # always sleep 2ms to give camera time to adjust
    sleep(2)
    # file=f"{datetime.now()}.jpg"
    # camera.capture(file)
    camera.capture("dex.jpg")

def soundCallback(channel):
    global timer
    global counter

    if GPIO.input(channel):
        print ('🔔', datetime.now())
        timer = datetime.now()
        counter +=1
        # if time between rings <500ms, add to counter
        if getDelta(datetime.now()) > 1:
            print('resetting')
            counter = 0
        if counter >= 3:
            print('✨📸✨')
            takePicture()
            upload()
            counter = 0
            sleep(10)

# Base function to send messages to Slack. It's just hitting the endpoint with the token and channel
def send():
    blocks=[{
        "type": "image",
			"title": {
				"type": "plain_text",
				"text": "🔔",
				"emoji": True
			},
			"image_url": "dex.jpg",
			"alt_text": "🔔"
            }]
    client.chat_postMessage(channel=SLACK_APP_CHANNEL, text="🔔")

def upload():
    try:
        name=f"{datetime.now()}.jpg"
        client.files_upload_v2(channel=SLACK_APP_CHANNEL, file="./dex.jpg", filename=name, initial_comment="🔔")
    except:
        print('Error uploading')

GPIO.add_event_detect(CHANNEL, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(CHANNEL, soundCallback)

while True:
    sleep(1)

# def main():
   


# if __name__ == '__main__':
#     while True:
#         main()
#         sleep(1)



