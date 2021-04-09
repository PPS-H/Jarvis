import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random

# sapi5 is provided by windows which enables us to use inbuilt windows voices...
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!!")

    else:
        speak("Good evening!!")

    speak("I am jarvis  . How may i help you.")

def takeCommand():
    # it takes users voice from microphone and returns the voice as a string
    r=sr.Recognizer()   #helps to Recognizer audio
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1 # it means that if user stops for one second while speaking then speech_recognizer will not complete the face ..it waits for one second.
        r.energy_threshold=700
        audio=r.listen(source)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}")
        except Exception as e:
            print('say that agian please')
            return "None"
        return query

def randomSongs():
    pass 

if __name__=='__main__':
    wishMe()
    # logic to do tasks according to the user 
    while True:
        query=takeCommand().lower()
        if 'wikipedia'in query:
            speak("Searching wikipedia")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(f"According to wikipedia   {results}")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open telegram' in query:
            tel_path='C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram'
            os.startfile(os.path.join(tel_path))
        elif 'open code' in query:
            vsCode_path='C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code'
            os.startfile(os.path.join(vsCode_path))
        elif 'play music' in query:
            music_dir='D:\\All songs'
            songs=os.listdir(music_dir)#give us the list of all files in the directory
            length=len(songs)-1
            song_number=random.randint(0,length)
            os.startfile(os.path.join(music_dir,songs       [song_number]))
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        elif 'quit' or 'exit' in query:
            speak("Thanks to use me  . We will meet again soon")
            break