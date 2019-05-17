import csv

def readUser():
    pass

def writeUser(user):
    with open('users.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user.values())
