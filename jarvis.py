import pyttsx3
import speech_recognition as sr


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     engine.setProperty('voice', voice.id)
#     engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing ...")
        query = r.recognize_google(audio, language='en-PH')
        print(query)
    except Exception as e:
        print(e)
        say("say that again please...")

    return query


say("Hello World")
said = take()
say(said)
