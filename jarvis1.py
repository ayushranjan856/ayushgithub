from multiprocessing.sharedctypes import Value
import re
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random


list1=[0, 1, 2]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2020423291.ayush@ug.sharda.ac.in', '2020423291.ayush')
    server.sendmail('ayush02sonu1@gmail.com', to, content)
    server.close()

if _name_ == "_main_":
    wishMe()
    # while True:
    if 1:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")


        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print("Time: ", strTime)
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "2020423291.ayush@ug.sharda.ac.com"
                sendEmail(to, content)
                speak("email has bean sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")