#!/usr/bin/env python3
"""
les differentes taches à executer
envoyer e-mail
ouvrir n'importe quel application
ouvrir n'importe quel dossier
ecouter de la musique

"""
import cmd
import os
import glob
#import wikipedia
import webbrowser
import smtplib


#task to do for

#openfile
def open(str):
    print("action ouverture file")

def determinetypefile(str):
    print("determiner le type de fichier à ouvrir")
    #a voir apres 
def ecoutermusique(str):
    songdir = "la ou tu met tes musiques"
    print("chercher dans les lists ou se trouve les musiques")
    print("sauf si y'a pas dans les fichier des musiques esayer de chercher dans les autres documents ")
    songs = os.listdir("la ou tu met des musiques")
    os.startfile(os.path.join(song_dir, son))

def delete(str, bool):
    print("supprimer le fichier str sur tout l'ordi ou pas")

def searchwiki(str):
    if 'wikipedia' in str.lower():
        print('looking at wikipedia')
        str = str.replace('wikipedia', '')
        """result = wikipedia.summary(str,sentences = 2) rechercher exemple d'utilisation du module wikipedia
        print(result)
        speak(result)
        """
def openyoutube(str): #rechercher exemple par rapport au module web browser et comment ouvrir un site 
    if 'open youtube' in str.lower:
        print("ouverture de youtube")
        """
        chercher comment ouvrir un site avec chrome
       """

def timeandmeteo():
    strtime = datetime.datetime.now().strtime("%H:%M:%S")
    #chercher comment avoir la meteo en python

def openapp():
    #chercher comment ouvrir une application en python

def sendemail(to, content): #tres dangereux  chercher smtplib exemple
    server = smtplib.SMTP('smtp.gmail.com', 587) #
    server.ehlo()
    server.starttls()
    sever.login('put your email', 'password')
    server.sendmail("destinator",to,content)
    server.close() 
