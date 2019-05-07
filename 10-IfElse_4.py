from datetime import datetime

helloIntent = ["hello","hi","hey","hi there","hey there"]
dateIntent = ["date","date please","tell me date","date today","what's the date"]
chat = True
while chat:
    msg = input("Enter your message : ")

    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        date = datetime.now().date()
        print(date.strftime("%d/%m/%y, %a"))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
