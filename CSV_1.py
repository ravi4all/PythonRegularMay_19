import csv

users = [
    {"name":"Sachin","score":100,"avg":55},
    {"name":"Virat","score":120,"avg":52},
    {"name":"Dhoni","score":50,"avg":53},
    {"name":"Yuvraj","score":70,"avg":51},
    {"name":"Rohit","score":40,"avg":50},
    ]

with open("data.csv",'w', newline='') as file:
    writer = csv.writer(file)
    for data in users:
        writer.writerow(data.values())
