import random

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour<=12:
        speak("good morning")
    elif hour> 12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello sir. please tell me how can i help you")




if __name__ == "__main__":
    wish()
    # takeCommand()
    # speak("hello sir")
    while True:
        if 1:

            query = takeCommand().lower()

            # logic building for tasks
            if "open notepad" in query:
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in query:
                os.system("Start cmd")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in query:
                music_dir = "C:\\Users\\sagar kumar yadav\\Desktop\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                # os.startfile(os.path.join(music_dir, rd))
                for song in songs:
                    if song.endswith('mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is: {ip}")

            elif "wikipedia" in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in query:
                speak("sir, what should i search on google")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif "send message" in query:
                kit.sendwhatmsg("+919123161902", "this is testing protocol", 9, 12)




            elif "close" in query:
                break;




