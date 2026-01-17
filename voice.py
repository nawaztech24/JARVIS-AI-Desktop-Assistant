import pyttsx3

def say(text):
    try:
        engine = pyttsx3.init("sapi5")   
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  
        engine.setProperty('rate', 170)

        print("NOVA says:", text)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Voice error:", e)
