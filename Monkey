import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('lstening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'monkey' in command:
                command = command.replace('monkey', '')

    except:
        pass
    return command

def run_monkey():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
        run_monkey()

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        talk('it is' + time)
        print(time)
        run_monkey()
        #if time[] == ''

    elif 'who is' in command:
        wiki = command.replace('who is', '')
        info = wikipedia.summary(wiki, 1)
        talk(info)
        print(info)
        run_monkey()

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
        run_monkey()

    elif 'go to sleep' in command:
        talk('okay see you later')

    else:
        talk('could you please repeat that?')
        run_monkey()

run_monkey()
