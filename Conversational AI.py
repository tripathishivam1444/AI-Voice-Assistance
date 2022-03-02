# सबसे पहले हम ये सारे Packeges install करेंगे by "pip install <Package Name>"
# Please Make your Wolframalpha Account and take your API and paste below at line 46

import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# for v in voices:
#     print(v)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('Hey my name is sam, I am python bot')


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        ask = r.recognize_google(audio, language='en-us')
        print(f"You said : {ask}")
    except Exception:
        print("Say that again...")
        return ""

    return ask


if __name__ == "__main__":
    while True:
        query = command().lower()
        print(query)




# Error को handel करने के लिए ।
        try:
            if 'Sam' in query:
                query = query.replace('Sam', '')
                client = wolframalpha.Client("L8R452-VW7TYWTQV4")  # Paste Your API Key Here....!!!
                res = client.query(query)
                ans = next(res.results).text
                print(ans)
                speak(ans)

        except Exception:
            try:
                query = query.replace('Sam', '')
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

            except Exception:
                try:
                    query = query.replace('Sam', '')
                    webbrowser.open('https://google.com/?#q=' + query)

                except:
                    print("It is weird but I got nothing try re-running the program")
                    speak("It is weird but I got nothing try re-running the program")
