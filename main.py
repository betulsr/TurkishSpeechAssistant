import speech_recognition as sr
from datetime import datetime
import webbrowser
import time

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            print('anlayamadim')
        except sr.requestError:
            print('sistem calismiyor')
        return voice

def response(voice):
    if 'nasilsin' in voice:
        print('iyi senden')
    if 'saat kac' in voice:
        print(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        url= 'https:/google.com/search?q='+ search
        webbrowser.get().open(url)
        print(search + 'icin bulduklarim')
    if 'tamamdir' in voice:
        print('gorusuruz')
        exit()

print('nasil yardimci olabilirim')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
