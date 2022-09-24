import pyttsx3
import datetime
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print("number  0 " + voices[0].id)  # david
# print("number  1 " + voices[1].id)  # ravi
# print("number  2 " + voices[2].id)  # mark
# print("number  3 " + voices[3].id)  # heera
# print("number  4 " + voices[4].id)  # zira
engine.setProperty('voice', voices[4].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<4:
        speak("Hey! What's up. Its time to sleep man. Lets play a game. ")
    elif hour>=4 and hour<12:
        speak("Hey! What's up. Hopefully you are enoying your morning. Lets play a game ")
    elif hour>=12 and hour<17:
        speak("Hey! Its energetic day. Lets play a game HAHA!. ")
    else:
        speak("Hey what's up buddy.. You are coding at night. And Its Awesome...!. ")
    # speak("And by the way. If you don't know me. I am assistant of Quick codes")

def takeCommand():
    ''' It takes input from microphone
    and give string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

def gameWin(comp, query):
    try:
        global you
        if "stone" in query:
            you = "stone"
            if comp=="paper" or comp == "scissors":
                speak("you win")
            else:
                speak("Our match is draw")
        elif "paper" in query:
            you = "paper"
            if comp=="stone" or comp=="scissor":
                speak("you win")
            else:
                speak("Our match is draw")
        elif "scissor" in query:
            you = "scissor"
            if comp=="stone" or comp=="paper":
                speak("You win")
            else:
                speak("Our match is draw")
        else:
            speak("Different minded")


    except:
        raise SyntaxError("Please enter valid input. ")


if __name__ == '__main__':
    wishMe()
    speak("Lets play a stone paper scissors game")
    # speak("Hello I am your new voice assistant. Thank you for this oportunity. Hopefully you Love my Voice...")
    while True:
        randNo = random.randint(1, 3)
        if randNo == 1:
            comp = 'stone'
        elif randNo == 2:
            comp = 'paper'
        elif randNo == 3:
            comp = 'scissors'

        speak(" I already choose my option ")
        speak(" Its your turn choose from: Stone, Paper or scissors . Or if you want exit say Exit or Quit")
        query = takeCommand().lower()
        if "exit" in query :
            speak("Nice to meet You! By By")
            exit()
        elif "quit" in query:
            speak("Nice to meet You! By By")
            exit()
        a = gameWin(comp, query)

        speak(f"I choosed {comp}")
        speak("Its all about fun...! Lets Play again....")














