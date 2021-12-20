import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

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

    speak("Hello I m John Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    ch= takeCommand().lower()
    if(ch!='jarvis'):
        speak(f"i m not {ch}")
    while(True):
        query = takeCommand().lower()
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how was your day' in query:
            speak('My day was fine sir hope you were also enjoying todays day...')
        elif ' fuck you' in query:
            speak('fuck you too sir')
        elif 'i love you' in query:
            speak('thanks sir same to you')
        elif ' who are you' in query:
            speak('I m a program created by Shivang malhotra...')
        elif 'how are you' in query:
            speak('I m fine sir hope you are also fine...')

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif ' open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        ch= takeCommand().lower()
