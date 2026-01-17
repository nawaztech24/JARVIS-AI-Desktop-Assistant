import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.energy_threshold = 300

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing (English)...")
        query = r.recognize_google(audio, language="en-IN")
    except:
        try:
            print("Recognizing (Hindi)...")
            query = r.recognize_google(audio, language="hi-IN")
        except:
            query = ""

    print("User said:", query)
    return query
