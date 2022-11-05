import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import io
import pygame

from gtts import gTTS

pygame.mixer.init()

import speech_recognition as sr
r = sr.Recognizer()

def stt(lang,dr):
    with sr.Microphone() as source:
        audio = r.record(source,duration=dr)        
        try:
            talk = r.recognize_google(audio,language='th-TH')              
        except sr.RequestError as e:
            talk = ""
            pass
        except sr.UnknownValueError:
            talk = ""
            pass
    return talk

def tts(my_text,language):
    print(my_text)
    with io.BytesIO() as f:
        speak = gTTS(text=my_text, lang=language)
        speak.save("temp_speak.mp3")
        pygame.mixer.music.load("temp_speak.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

