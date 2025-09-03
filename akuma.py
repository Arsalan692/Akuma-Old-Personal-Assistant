
from tkinter import *

import pyttsx3
#for the speaker to speak
import datetime
#for the maintaince of date and time
import speech_recognition as sr

import wikipedia
#total wikipedia
import smtplib

import webbrowser as wb

import psutil

import pyjokes

import os

from PIL import Image, ImageTk
#pillow
import pyautogui

import random

import json
#for news
import requests
#for news
from urllib.request import urlopen
#for news
import wolframalpha
#pip install wolframalpha
import time as t
#pip already pre-installed library.

engine = pyttsx3.init('sapi5')
wolframalpha_app_id = '6R7223-9AHJ3LVH2K'

my_name = "Arsalan"

def my_speaker(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time  = datetime.datetime.now().strftime("%I:%M:%S")
    my_speaker(f"The current time is {Time}")


def screenshot():
    image = pyautogui.screenshot()
    image.save(r"C:\Users\123\Pictures\Screenshots\screenshot.png")


def day1():
    day = datetime.datetime.now().day
    my_speaker(f"Current day is {day}")


def date():
    date = datetime.datetime.now().date()
    my_speaker(f"the current date is {date}")


def num123456():
    x = range(0, 6)
    for y in x:
        return y


def wish_me():
    my_speaker(f"Welcome back {my_name}!")
    time()
    day1()
    # addition of greetings
    hour = datetime.datetime.now().hour
    if hour>6 and hour<12:
        my_speaker(f"Good Morning {my_name}! ")
    elif hour>=12 and hour<18:
        my_speaker(f"Good afternoon {my_name}!")
    elif hour>=18 and hour<24:
        my_speaker(f"good evening {my_name}! ")
    else:
        my_speaker(f"good night {my_name}! ")

    my_speaker(f"Akuma at your service. How can I help you {my_name}.")


def email_sender(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    # Required low security for the execution

    server.login("hackerakuma698@gmail.com", "Hackers@123")
    server.sendmail("hackerakuma698gmail.com", to, content)
    server.close()


def voice_listner(): # listen voice and give output in words
    p = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.... ")
        p.pause_threshold = 1
        p.energy_threshold = 300
        p.adjust_for_ambient_noise(source, duration=1)
        audio_of_person = p.listen(source)

    try:
        print('Recognizing......')
        query = p.recognize_google(audio_of_person)
        print(query)
    except Exception as e:
        print(e)
        print("Say it again please...")
        return "none"
    return query


def cpu_and_battery():
    cpu = str(psutil.cpu_percent())
    my_speaker(f"Cpu is at {cpu} percentage. ")
    #cpu info

    battery = str(psutil.sensors_battery())
    my_speaker(f"battery is at {battery} percentage.")

    #battery percentage..


def jokes():
    my_speaker(pyjokes.get_joke())



if __name__ == '__main__':

    wish_me()


    while True:
        query = voice_listner().lower()

        if "time" in query:
            time()
        if "date" in query:
            date()
        if "day" in query:
            day1()
        if "wikipedia" in query:
            my_speaker("searching.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            my_speaker("According to wikipedia..")
            print(result)
            my_speaker(result)

        if "send email" in query:

            try:
                my_speaker("What should I say? ")
                content = voice_listner()
                my_speaker("Who is your reciever")
                for_email = input("Enter the person's email: ")
                to =  for_email
                email_sender(to, content)
                my_speaker(content)
                my_speaker("Email has been send.")


            except Exception as e:
                print(e)
                print("Enable to send your email!")
                my_speaker('Failed to send email! ')

        if "search in chrome" in query:
            my_speaker("what do you want to search? ")
            my_chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            # location of chrome path on my PC

            search = voice_listner().lower()
            wb.get().open_new_tab(f"https://www.{search}.com")
            # workable only with extensions of .com


        if "search on youtube" in query:
            my_speaker("What do you want to search? ")
            search_term = voice_listner().lower()
            my_speaker("Here we go on youtube.. ")
            wb.open('https://www.youtube.com/results?search_query='+search_term)


        if "search on google" in query:
            my_speaker("what do you want to search.. ")
            search_google = voice_listner().lower()
            wb.get().open_new_tab('https://www.google.com/search?q='+search_google)


        if "cpu" in query:
            cpu_and_battery()


        if  "battery" in query:
            cpu_and_battery()


        if "joke" in query:
            jokes()

        if "go offline" in query or "goa fine" in query:
            my_speaker("going offline")
            quit()

        if  "akuma sleep" in query or "katto" in query:
            my_speaker("going offline")
            quit()
        if 'virtualbox' in query:
            my_speaker("opening virtual box.. ")
            virtual_box_path = r"D:\virtual box 1\VirtualBox.exe "
            os.startfile(virtual_box_path)


        if "write a note" in query:
            my_speaker("What to do you want write.. ")
            notes = voice_listner()
            file = open("notes.txt", "w")
            my_speaker("should I include date and time. ")
            answer_to_include = voice_listner()
            if "yes" in answer_to_include or "sure" in answer_to_include:
                time_in_notes = datetime.datetime.now().strftime("%I:%M:%S")
                date_in_notes = datetime.datetime.now().date()
                modify_date1 = f"{date_in_notes}"
                file.write(modify_date1)
                file.write(", ")
                file.write(time_in_notes)
                file.write(":-")
                file.write(notes)
                my_speaker("Done taking notes. ")
            else:
                file.write(notes)

        if "who is my mother" in query:
            my_speaker("your mother name is saira shafique.")



        if "show notes" in query:
            my_speaker("showing notes")
            file = open("notes.txt","r")
            print(file.read())
            my_speaker(file.read())

        if "screenshot" in query:
            screenshot()


        if "play music" in query or "koi music baja" in query:
            path_of_songs = r"D:\songs"
            music = os.listdir(path_of_songs)
            my_speaker("what should I play?")
            my_speaker("select a number.")
            answer = voice_listner().lower()

            while("play" not in answer and answer!="random" and  answer!="number zero" and answer!="koi bhi" and answer!="mohit favourite" and answer!="mohit ka favourite"):
                my_speaker("I could not understand you, please try again. ")
                answer = voice_listner().lower()
            if "play" in answer:

                splitted = answer.split()
                for single in splitted:
                    if single == "zero" or single=="0":
                        num =0
                    elif single == "one":
                        num = 1

            elif "mohit favourite" in answer or "mohit ka favourite" in answer:
                num = 2

            elif "random" in answer or "koi bhi" in answer:
                num = random.randint(0, 1)

            os.startfile(os.path.join(path_of_songs, music[num]))

        if "my best friends" in query:
            my_speaker("Your best friends are ahad, saim and mueed")

        if "remember that" in query:
            my_speaker("What should I remember")
            memory = voice_listner().lower()
            my_speaker("You asked me to remember that "+memory)
            memory_notes = open("memory.txt","w")
            memory_notes.write(memory)
            memory_notes.close()

        if "do you remember anything" in query:
            memory_notes = open("memory.txt", "r")
            my_speaker("you asked me to remember that"+memory_notes.read())

        if "news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/everything?q=tesla&from=2021-02-08&sortBy=publishedAt&apiKey=0a9cfa281b9f47dd8edaecd59c13a922")
                data = json.load(jsonObj)
                x = 1

                my_speaker("Here are some news")
                print("==============" + "\n")                                                            #split remember to make it easier
                for item in data["articles"]:
                    print(str(x) + "." + item['title'] + '\n')
                    print(item['description'] + "\n")
                    my_speaker(item['title'])
                    x += 1
            except Exception as e:
                print(str(e))
        if "where is" in query:
            query = query.replace("where is","")
            location = query
            my_speaker("locating"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        if "calculate" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx  = query.lower().split().index("calculate")
            query = query.split()[indx + 1:]
            res = client.query("".join(query))
            answer = next(res.results).text
            print("The answer is: "+answer)
            my_speaker("The answer is "+answer)

        if "do you know about" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                my_speaker(next(res.results).text)
            except StopIteration:
                print("No results")

        if "stop listening" in query:
            my_speaker("how much seconds should I not listen to your commands sir! ")
            answer1 = int(voice_listner())
            t.sleep(answer1)
            print(answer1)

        if 'log out' in query:
            os.system("shutdown -l")

        if 'restart' in query:
            os.system("shutdown /r /t 1")

        if "shutdown" in query:
            os.system("shutdown /s /t 1")

        if "who are you" in query:
            my_speaker("I am Akuma , A personal AI assistant , I am created by Arsalan.")

        if "hello" in query:
            my_speaker("Hey")

        if "how are you" in query:
            my_speaker("I am fine, thanks for asking, how are you sir! ")

        if "who am i" in query:
            my_speaker("if you can talk, its means you are a human")

        if "why you came to this world" in query:
            my_speaker("thanks to Arsalan, further this is a secret")

        if "tell me about your creator" in query or "who is your creator" in query:
            my_speaker("my creator is arsalan, he is 16 years old and thanks to him that he created me")

        if "brother" in query:
            my_speaker("the name of your brother is zarar,he is a web developer")        #file transfer from a local device!

        if "father" in query:
            my_speaker("the name of your father is Shafiq Ahmed Sheikh , he works in Philip Morris International")

        if "mueed" in query or "mohit" in query:
            my_speaker("mueed is an idiot person but a very handsome and good looking friend of my creator arsalan , well I don't like him personally")

        if "thank you" in query:
            my_speaker("my pleasure ")

        if "saim introduction" in query:
            my_speaker("He is a fucking idiot and friend of my creator. ")





