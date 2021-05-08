import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def PyAudioBook():
    book = open('oop.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    speaker = pyttsx3.init()
    for num in range(7, pages):
        page = pdfReader.getPage(7)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()

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

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        talk('it is' + time)
        print(time)

    elif 'who is' in command:
        wiki = command.replace('who is', '')
        info = wikipedia.summary(wiki, 1)
        talk(info)
        print(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)

    elif 'go to sleep' in command:
        talk('okay see you later')

    elif 'bangla song' in command:
        song = 'bangla song'
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'good morning' in command:
        talk('good morning hasib')


    elif 'good evening' in command:
        talk('good evening hasib')


    elif 'good night' in command:
        talk('good night hasib')

    elif 'good afternoon' in command:
        talk('good night hasib')

    elif 'how are you' in command:
        talk('I am doing good. Thank you')

    elif 'your name' in command:
        talk('my name is Monkey')

    elif 'change your voice' in command:
        engine.setProperty('voice', voices[1].id)
        talk('Sure')

    elif 'read book' in command:
        PyAudioBook()

    else:
        talk('could you please repeat that?')

while True:
    run_monkey()
