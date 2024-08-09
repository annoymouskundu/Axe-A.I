import os
import webbrowser

import speech_recognition as sr


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://www.wikipedia.com"],]
        for site in sites:
            if "Open {site[0]}".lower() in query.lower():
                say("Opening {site[0]} sir...")
                webbrowser.open(site[1])


        #say(query)