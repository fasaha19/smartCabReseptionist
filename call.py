# Initilizing the file.....
import datetime
import time
from twilio.rest import Client
import requests
import speech_recognition as sr


# Account Sid and Auth Token from twilio.com/console
account_sid = 'AC157912d1dc45d999e6d347d9f4b958fc'
auth_token = 'ec58c8c7c183268af7e3ef33619c129a'
client = Client(account_sid, auth_token)

# Creating the recording list
recordings = client.recordings. list(date_created_after=datetime.date.today())
temp = len(recordings)
print(datetime.date.today())
print(temp)


#initilizing the recroding process.....

while (True):
    recordings = client.recordings. list(date_created_after=datetime.date.today())
    print(datetime.datetime.now())
    n = len(recordings)
    print(n)
    if(n > temp):
        time.sleep(11)
        print(recordings[0])
        c=recordings[0].sid
        print(c)
        z=c+".wav"
        temp=n
        n=n+1
#downloading the recorded file....

        res=requests.get(r"https://api.twilio.com/2010-04-01/Accounts/AC157912d1dc45d999e6d347d9f4b958fc/Recordings/"+c)
        print("file downloading........")
        with open(c+".wav",'wb')as f:
            f.write(res.content)

### speecch recognizing.......

        r = sr.Recognizer()

        audio = z

        with sr.AudioFile(audio) as source:
            print("Speech to text recognition processing!!!!")
            audio = r.record(source)
            
        try:    
            text = r.recognize_google(audio)
            print (text)

        except Exception as e:
            print(e)

### Messaging to the driver......

        print("Messaging to the driver......")
        message = client.messages \
        .create(
             body=(text),
             from_='+12016546959',
             to='+918754908523'
         )

        print(message.sid)
