import csv

users = []

with open('data.csv') as file:
    reader = csv.reader(file)
    for data in reader:
        user = {"name":data[0],"score":data[1],"avg":data[2]}
        users.append(user)
print(users)
