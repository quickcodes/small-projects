import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import turtle
import time
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[4].id)


def speak(audio):
    # speak the given input
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    os.system("color f0")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am your desktop assistant. Tell me how can i help you")


def takeCommand():
    # print("hello")
    # it takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\tListening...")
        r.pause_threshold = 1
        # r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("\tRecognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"\tUser said: {query}\n\t")
    except Exception as e:
        # print(e)
        print("\tSay that again please..")
        return "\tNone"
    return query


# Display the program's instructions.
def stopwatch():
    print("\tStarted")
    speak('\tStarted... Press any key for lap. and q to finish')
    startTime = time.time()  # get the first lap's start time
    lastTime = startTime
    lapNum = 1
    try:
        while True:
            if input() == 'q':
                break
            lapTime = round(time.time() - lastTime, 2)  # 2 shows number's after decimal
            totalTime = round(time.time() - startTime, 2)
            print('\tLap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time()
            # reset the last lap time
    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying.
        print('\n\tDone.')


def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size / 3)
            turtle.left(216)
            turtle.end_fill()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for exicuting task on query
        if 'exit' in query:
            exit()
        elif 'quit' in query:
            exit()
        elif 'home' in query:
            exit()
        elif 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("\t", results)
            speak(results)
        elif 'youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")
        elif 'google' in query:
            speak('Opening google')
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            speak('Opening stackoverflow')
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            speak('playing music')
            music_dir = 'E:\\programs\\songs'
            songs = os.listdir(music_dir)
            print("\t", songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'downloader' in query:
            speak('Opening youtube downloader')
            yt_dir = 'E:\\programs\\python\\YouTube downloader'
            app = os.listdir(yt_dir)
            print("\t", app)
            os.startfile(os.path.join(yt_dir, app[1]))
        elif 'game' in query:
            speak('Opening stone paper scissor')
            game_dir = 'E:\\programs\\python\\basics\\games'
            game = os.listdir(game_dir)
            print("\t", game)
            os.startfile(os.path.join(game_dir, game[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'weather' in query:
            speak("Please enter the name of city")
            folder = 'E:\\programs\\python\\Desktop Assistant'
            weather = os.listdir(folder)
            os.startfile(os.path.join(folder, weather[1]))
        elif 'stopwatch' in query:
            speak("opening stopwatch...")
            stopwatch()
        elif 'sublime' in query:
            subprocess.Popen("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
        elif 'visual' in query:
            subprocess.Popen("C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'pycharm' in query:
            subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe")
        # elif 'whatsapp' in query:
        #     subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe")
        elif 'notepad' in query:
            note_dir = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            note = os.listdir(note_dir)
            os.startfile(os.path.join(note_dir, note[2]))
        elif 'reader' in query:
            speak("Please select a text file")
            read_folder = 'E:\\programs\\python\\Desktop Assistant'
            reader = os.listdir(read_folder)
            os.startfile(os.path.join(read_folder, reader[2]))
        elif 'star' in query:
            speak("Drawing amazing star")
            a = turtle.Turtle()
            a.getscreen().bgcolor("black")
            a.penup()
            a.goto(-200, 100)
            a.pendown()
            a.color("yellow")
            a.speed(25)
            star(a, 360)
            turtle.done()
        elif 'tell' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            query = query.replace("something", "")
            query = query.replace("about", "")
            query = query.replace("ok", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Internet")
            print("\t", results)
            speak(results)
