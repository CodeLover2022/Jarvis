import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import pyaudio
# pip install pipwin pipwin install pyaudio

engine=pyttsx3.init('sapi5') #'sapi5' is a Microsoft speech API
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[0].id) #voive[0]->male voice,voice[1]->female Voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am Jarvis  Please Tell me how may I help you")
def command():          #it takes microphone from the user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__=="__main__":
    #speak("Priyanshu is a good boy")
   WishMe()
while True:
      query=command().lower()
      if 'wikipedia' in query:
          speak('Searching wikipedia')
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to Wikipedia")
          speak(results)
      elif 'go to sleep' in query:
          speak("I am going to sleep,sir")
          exit(0)
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open google' in query:
          webbrowser.open("google.com")
      elif 'play music' in query:
          music_dir='C:\\Users\\PRIYANSHU\\Documents\\songs'
          songs=os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))
      elif 'the time' in query:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir,the time is:{strTime}")
      elif 'open android studio' in query:
          codePath="C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
          os.startfile(codePath)


