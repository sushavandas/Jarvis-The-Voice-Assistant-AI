import pyttsx3


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    print(voices)
    engine.say(text)
    engine.runAndWait()

speak("india is my contry, all indians are my brother and sister")