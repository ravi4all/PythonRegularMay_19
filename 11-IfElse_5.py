from datetime import datetime
import os, random
import glob

helloIntent = ["hello","hi","hey","hi there","hey there"]
dateIntent = ["date","date please","tell me date","date today","what's the date"]
musicIntent = ["play music","play song","start music"]
chat = True
while chat:
    msg = input("Enter your message : ")

    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        date = datetime.now().date()
        print(date.strftime("%d/%m/%y, %a"))
    elif msg in musicIntent:
        os.chdir(r"C:\Users\asus\Music")
        #songs = os.listdir()
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
