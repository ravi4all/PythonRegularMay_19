'''
names = ["Ram","Shyam","Goapl","Rohan"]
marks = [56,67,65,87]
grades = ['b','b+','b+','a']
students = {"names":names,"marks":marks,"grade":grades}
'''

students = [
    {"name":"Ram","marks":[78,65,88],"grade":'A'},
    {"name":"Shyam","marks":[56,78,90],"grade":'A+'},
    {"name":"Raman","marks":[76,78,44],"grade":'B+'},
    {"name":"Aman","marks":[67,76,72],"grade":'A'},
    {"name":"Suresh","marks":[90,98,89],"grade":'A+'},
    {"name":"Jatin","marks":[56,67,54],"grade":'B'}
    ]

#1. Find all the students whose grades are A or A+
for i in range(len(students)):
    if students[i]['grade'] == 'A+' or students[i]['grade'] == 'A':
        print(students[i]["name"],students[i]["marks"],students[i]["grade"])

print("-------------")
#2. Find average marks of all students
for i in range(len(students)):
    marks = students[i]['marks']
    avg = sum(marks) // len(marks)
    print(students[i]["name"],avg)
