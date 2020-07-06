import pyttsx3                              #pip install pyttsx3
import speech_recognition as sr             #pip install speechRecognition
import datetime
import wikipedia                            #pip install wikipedia
import os
import smtplib
import random
import webbrowser
import time
import socket
import requests                                 #pip install requests
print("initializing deeps")
MASTER='Deeepaa'
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)        #set voices[0] for male voice

# will speak the string being passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#This function wishes the user
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('Hii  '+MASTER+'....Good Morning ! How can i help you?? ')
    elif hour>=12 and hour<=17:
        speak('Hii  '+MASTER+'....Good Afternoon! How can i help you ?? ')
    else:
        speak('Hii  '+MASTER+'....Good Evening ! How can i help you ??  ')


#for taking commands
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #speak("Listening...")
        audio=r.listen(source)
    try:
        print("Recognising")
        #speak("recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
        speak("you said "+query)
    except Exception as e:
        speak("Sorry , say that again!")
        print(e)
        query=takecommand()
    return query


#for sending mail
def send_mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your mail id','Your app password')
    server.sendmail('your mail id',to,content)
    server.close()

speak(" Initializing deepsss...")
wishme()

jokes=['Why is it   PERSON and not ..PERDAUGHTER?? Hahaha','Can a kangaroo jump higher than a building?....offcouse yes,..buildings cannot jump... hahaha','You are so beautiful! I love you....hahhahaha','You can break me without touching me, or even seeing me... What am I? Answer....A promise ...hahaha']


def start(query):
    if 'wikipedia' in query.lower():
        speak("searching wikipedia...")
        query=query.replace('wikipedia',"")
        result=wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)

    elif 'weather report' in query.lower() or 'weather' in query.lower():
        api_address='http://api.openweathermap.org/data/2.5/weather?q=Kolkata&appid= your app id '          #you can get it from openweathermap.org
        json_data=requests.get(api_address).json()
        data=json_data['weather'][0]['description']
        print(data)
        speak(data)


    elif 'introduce yourself' in query.lower() or 'hello' in query.lower() or 'tell me about yourself' in query.lower() or'who made you' in query.lower():
        speak("Hiii  !  I am deeepss created by Deepaa Pandey on 24th of may 2020 !!  I am a python assistant ....ready to help you with your queries....")

    elif 'what do you do' in query.lower() or 'how can you help' in query.lower() or 'more about you' in query.lower():
        speak("Deeeps can help you to automate your tasks such as search videos in YouTube and play them, send emails, open websites, search materials in Wikipedia and read them,inform weather forecast in your country,jell jokes,  greetings and more. ")
    elif 'hi' in query.lower():
        speak("Hii deeepaa, glad to talk to you!")

    elif 'how are you' in query.lower():
        speak("I am absolutely fine! Hope you are doing great too !")

    elif 'joke' in query.lower() or 'jokes' in query.lower() or 'say something funny' in query.lower() :
        joke=random.choice(jokes)
        speak(joke)

        #To display IP address
    elif 'ip address' in query.lower() or 'location' in query.lower():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        url='http://api.ipstack.com/'+str(ip_address)+'? access_key= Your acess key'  #You can get the acess key from ipstack
        response=requests.get(url).json()
        ip=response.get("ip")
        print(ip)
        continent=response.get("continent_name")
        print(continent)
        country=response.get('country_name')
        region=response.get('region_name')
        latitude=response.get('latitude')
        longitude=response.get('longitude')
        speak(f"{MASTER} your ip address is {ip} , you are present at {continent} in {country} at {region} and.. your latitude is {'%.3f'%latitude} ..and longitude is {'%.3f'%longitude}")


    elif 'open youtube' in query.lower():
        speak("Okay sure!.Deepa")
        #webbrowser.open("youtube.com")
        url="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        speak("Okay sure!.Deepa")
        url="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        speak("Okay sure!.Deepa")
        url="facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open reddit' in query.lower():
        speak("Okay sure!.Deepa")
        url="reddit.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
        speak("Okay sure!.Deepa")
        url="instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'time' in query.lower() or 'the time' in query.lower():
        t=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {t}")

    elif 'open code' in query.lower() or 'open vs code' in query.lower():
        speak("Okay sure!.Deepa")
        code_location="F:\\visualstudiocodes\\Code.exe"
        os.startfile(code_location)

    elif 'mail to' in query.lower() or 'mail' in query.lower():
        try:
            speak("Whom should i send the message ?")
            mail_id = takecommand()
            speak("What message   should   i   send?")
            command= takecommand()
            send_mail(str(mail_id),command)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

    elif 'bye deeps' in query.lower() or 'thanks bye' in query.lower() or 'goodbye' in query.lower() or 'good bye' in query.lower() or 'bye' in query.lower() :
        speak("Nice to talk to you deeepa!.. Good bye & have a nice day...")
        exit()

    else:
        speak("oops! sorry I'm clueless about it.....Please Search it on google!")
        url="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    # elif 'open music' in query.lower():
    #     music_location= specify the location of music in your system


while True:
    start(takecommand())
    time.sleep(3)
