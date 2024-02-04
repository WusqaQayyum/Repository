import speech_recognition as sr
import pywhatkit
from gtts import gTTS
from playsound import playsound


def speech(text):
    print(text)
    language = "en"
    output=gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")



def check():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"you said {text}")

    if "youtube" in text.lower():
        speech("okay, searching for that on youtube")
        pywhatkit.playonyt(text)

    elif "what is your name" in text.lower():
        speech("My name is Princess Wusqa")

    elif "tell me a joke" in text.lower():
        speech("See YourSelf In The Mirror")

    else: #search on Google
        speech("okay, Searching For That On Google")
        pywhatkit.search(text)

def assistant():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"you said {text}")

    if "hello princess" in text.lower():
        speech("Hello, How May I Help You")
        check()

    else:
        return


assistant()

