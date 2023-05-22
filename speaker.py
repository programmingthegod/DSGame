import pyttsx3
engine = pyttsx3.init()

class Speaker:
    def speak(msg):
        engine.say(msg)
        engine.runAndWait()