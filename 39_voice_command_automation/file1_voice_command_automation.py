# NOTE: Requires speech_recognition library
# pip install SpeechRecognition

import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("Command recognized:", command)
    except:
        print("Sorry, could not understand")

# Example
# listen_command()
