#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
from gtts import *
import pyttsx3
import datetime
import os
#import pythoncom


class SpeakList():
    def __init__(self):
        self.__word = None

    def Listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("i'm listenning")
            audio = r.listen(source)
        try:
            s = r.recognize_google(audio,Language = 'en-in')
            self.__word = s
            print(s.lower())
        except sr.UnknownValueError:
            print("Don't understand what you are saying mister")
        except sr.RequestError as e:
            print("Could not request results$; {0}".format(e))

    #the speak function of speakandlisten
    def speak(self, word):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(word)
        engine.runAndWait()
        print("voice len = {}".format(len(voices)-1))


    def print(self):
        if self.__word != None:
            print(self.__word)




class Task:
    def __init__(self):
        speakerlistener = SpeakList()

    def actuality(self):
        hour = int(datetime.datetime.now().hour)
        meteo = None
        print(hour)


a = SpeakList()
a.actuality()
a.speak("Junior")
a.Listen()
a.print()