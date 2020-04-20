#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
from gtts import *
import pyttsx3
from datetime import datetime
import os
import cmd
import glob
import wikipedia
import webbrowser
import smtplib
from playsound import playsound


class SpeakList():
    def __init__(self):
        self.__word = None
        self.dicolang = {"francais":0 ,"english":1}
        self.curvoice = self.dicolang["english"]

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
        engine.setProperty('voice',voices[self.curvoice].id)
        engine.say(word)
        engine.runAndWait()


    def print(self):
        if self.__word != None:
            print(self.__word)




class Task:
    def __init__(self):
        speakerlistener = SpeakList()

    def wikisum(self,str):
        print('looking at wikipedia')
        result = wikipedia.summary(str,sentences = 2)
        return result

    def time(self):
        n = datetime.now()
        al = datetime.strftime(n,"%H:%M:%S").split(":")
        str = "it is {} hour {} minutes {} seconds".format(al[0],al[1],al[2])
        return str
    def playmusic(self,str):
        path = "C:\\Users\\lolej\\Music"
        musics = os.listdir(path)
        bool = False
        i = 0
        while i < len(musics):
            if str in musics[i]:
                bool = True
                break
            else:
                i +=1
        if i < len(musics) and bool == True:
            playsound(musics[i])
        return bool







    


a = SpeakList()
t = Task()
t.playmusic("Sing Me To Sleep")
