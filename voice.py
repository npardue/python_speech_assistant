import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    '''Sets default microphone as audio input source, and records user's speech to a variable voice_data. 
    If unable to understand the command given, will ask to repeat. If unable to connect to the internet, will alert that the 
    service is down.
    '''
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 2)

        if ask:
            speak(ask)
        
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I didn\'t catch that. Please repeat.')
        except sr.RequestError:
            speak('Sorry, my speech service is down.')
        return voice_data

def response(voice_data):
    '''Checks voice_data for stringed variables, and then speaks the appropriate response.
    '''
    if 'what is your name' in voice_data:
        speak('My name is Deckard')
    if 'who are you' in voice_data:
        speak('My name is Deckard')
    if 'search' in voice_data:
        search = record_audio('What\'re you looking for?')
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(f'Here are your results for "{search}".')
    if 'exit' in voice_data:
        speak('Safe travels.')
        exit()


def speak(audio_string):
    '''Creates and saves an audio file of what the TTS assistant says, plays the file, prints the file, 
    and then deletes the file.
    '''
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
speak('What can I do for you?')

while 1:
    #speak(f'You said: {voice_data}')
    voice_data = record_audio()
    response(voice_data)


