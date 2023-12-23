import os
import speech_recognition as sr
import pyttsx3
import datetime

 
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def process_command(command):
    if "hello" in command:
        return "Hello! How can I help you?"
    elif "how are you" in command:
        return "I'm doing well, thank you!"
    elif "how is today" in command:
        return "It's a good day!"
    elif "what time is it" in command:
        now = datetime.datetime.now()
        return f"It's {now.strftime('%H:%M')}"
    elif "thank you" in command:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that command."


with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            
            text = recognizer.recognize_google(audio, language='en-US')
            print("You said:", text)
            
            response = process_command(text.lower())
            print("Assistant:", response)
            
          
            engine.say(response)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

