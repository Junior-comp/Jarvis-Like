#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
from gtts import *

class SpeakList():
    def __init__(self):
        self.__word = None

    def Listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            s = (r.recognize_google(audio))
            self.__word = s
            print(s.lower())
        except sr.UnknownValueError:
            print("Don't understand what you are saying mister")
        except sr.RequestError as e:
            print("Could not request results$; {0}".format(e))

    def print(self):
        if self.__word != None:
            print(self.__word)

a = SpeakList()
a.Listen()
a.print()