from email import message
from numpy import take
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import random as r
from gtts import gTTS
import os
import subprocess as sp
import turtle
import pyjokes
from pywikihow import search_wikihow
from playsound import playsound
import pywhatkit as kit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()





   
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning , Jai Shree Ram ")
    elif hour>12 and hour<16:
        speak("Good afternoon , Jai Shree Ram ")
    else:
        speak("Good evening , Jai Shree Ram  ")

           
wishMe()

speak("I am activated , what tasks for today? ")
print("I am activated , what tasks for today? ")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
       print(" Listening.....")
       r.pause_threshold = 1
       r.energy_threshold = 4000
       audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return"Not recognised"
    return query

while True:
    query = takecommand().lower()
    print(query)
    if query==0:
        continue

    if 'new user' in query:
        speak("What's your name?")
        name ='Human'
        name = takecommand()
        speak("Hello, " + name + 'nice to meet you , I am a voice assistant , how may i help you ?',)

    if 'otp' in query:
        speak('genrating otp')
        def otpgen():
            otp=""
            for i in range(3):
                otp+=str(r.randint(0,9))
                otpgen()
        print(otpgen) 

    if'register' in query:
        speak("Registering new person :")
        speak(" what is your name?")
        name = 'name'
        name = takecommand()
    
        speak("You are registered as : "+name+'Thank you for regestering',)
        print("You are registered as : "+name+'Thank you for regestering',)

    if 'wikipedia' in query:
        speak('searching Wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wiki ")
        print(results)
        speak(results)

    

    if 'who are you' in query :
     speak(' I am a highly Functional voice assistant created by Priyanshu , specially desgined for his collaborative workspace.')

    if "what can you do"in query or "what do you do" in query:
        speak('I perform various tasks assigned to me , such includes - resarching or gathering information , performing multiple operations , managing multiple applications and the most important helping the team in Creation of Multiverse  ')

    
    if 'how to function' in query:
        speak('How to function is activated , please tell me what do you want to know')
        how = takecommand()
        max_results = 1
        how_to = search_wikihow(how, max_results)
        assert len(how_to) == 1
        how_to[0].print()
        speak(how_to[0].summary)

    
    if 'youtube' in query:
        speak('Opening Youtube')
        webbrowser.open("www.youtube.com")

    if 'search' in query:
        import wikipedia as googleScrap
        query = query.replace("search","")
        speak("This is what i found")
        kit.search(query)
        results = googleScrap.summary(query,2)
        print(results)
        speak(results)

    
    

    if 'gmail' in query:
        speak('opening gmail')
        webbrowser.open("mail.google.com/mail/u/1/#inbox")                     

    if "music site" in query or "song" in query:
        speak('which song ?')
        song = takecommand()
        query = query.replace("music.youtube.open",song)
        webbrowser.open("https://music.youtube.com/search?q=")
        

    if 'prabhu' in query or 'ram' in query or 'bhagwan' in query:
        speak("JAI SHREE RAM")
        playsound('C:\\Users\\priya\\Downloads\\narayan.mp3')
    
   
    if 'repeat' in query:
        speak('okay sir what do you want me to repeat')
        repeating_words = takecommand()
        speak(repeating_words)
   
    if'thanks' in query  or 'thank you' in query  or 'good work' in query  or 'nice job' in query  or 'job' in query:
        speak('Mention not , i was desgined to help you')  

    if 'time' in query:
     strTime=datetime.datetime.now().strftime("%H:%M:%S")
     speak(f"the time is {strTime}")
        
    
    if 'play music' in query or 'gana' in query:
        speak('ok sir ')
        playsound('C:\\Users\\priya\\Downloads\\02 - Sanam Re.mp3')
       
        


    if 'joke' in query:
        speak(pyjokes.get_joke())
        reply = takecommand()
        if 'funny' in reply:
            speak('I know hahahahaa')

    

    if 'message' in query:
        speak("what should the message contain")
        message=takecommand()
        kit.sendwhatmsg("+917037615297",message,19,24)

    elif "weather" in query:
        api_key="8ef61edcf1c576d65d836254e11ea420"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name=takecommand()
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
            str(current_temperature) +
            "\n humidity in percentage is " +
            str(current_humidiy) +
            "\n description " +
            str(weather_description))
            print(" Temperature in kelvin unit = " +
            str(current_temperature) +
            "\n humidity (in percentage) = " +
            str(current_humidiy) +
            "\n description = " +
            str(weather_description)) 
        else:
            speak(" City Not Found ")


    if "intresting" in query or "smile" in query or "what else"in query:
        speak('ok just wait and watch')
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        t = turtle.Pen()
        turtle.bgcolor('black')
        for x in range(360):
            t.pencolor(colors[x%6])
            t.width(x//100 + 1)
            t.forward(x)
            t.left(59)

            if 0xFF == ord('a'):
                    break

    if "good bye" in query or "bye" in query :
        speak('rudra is being switched off , have great day sir ')
        break

    elif "stop" in query or "deactivate" in query:
        speak('Deactivated')

        print('Deactivated ')
        break


    
    
    
    

    

    



