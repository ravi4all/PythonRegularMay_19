Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 12,
>>> x
(12,)
>>> x = (12,)
>>> x
(12,)
>>> x = (12,23,45,67,78)
>>> x = 12,23,45,67,78
>>> x
(12, 23, 45, 67, 78)
>>> x[0]
12
>>> x[0:3]
(12, 23, 45)
>>> x[-1]
78
>>> x[0] = "hello"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x[0] = "hello"
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> student = name, marks, grade = 'Ram', 78, 'A'
>>> name
'Ram'
>>> marks
78
>>> grade
'A'
>>> student
('Ram', 78, 'A')
>>> name = 'Shyam'
>>> student
('Ram', 78, 'A')
>>> student = {"name":"Ram",marks:78,"grade":'A'}
>>> student["name"]
'Ram'
>>> student[marks]
78
>>> student[78]
78
>>> student = {"name":"Ram","marks":78,"grade":'A'}
>>> student["marks"]
78
>>> student[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    student[0]
KeyError: 0
>>> student.keys()
dict_keys(['name', 'marks', 'grade'])
>>> student.values()
dict_values(['Ram', 78, 'A'])
>>> student.items()
dict_items([('name', 'Ram'), ('marks', 78), ('grade', 'A')])
>>> for data in student:
	print(data)

	
name
marks
grade
>>> for data in student.items():
	print(data)

	
('name', 'Ram')
('marks', 78)
('grade', 'A')
>>> student["hobby"] = "Cricket"
>>> student
{'name': 'Ram', 'marks': 78, 'grade': 'A', 'hobby': 'Cricket'}
>>> names = ["Ram","Shyam","Goapl","Rohan"]
>>> marks = [56,67,65,87]
>>> grades = ['b','b+','b+','a']
>>> students = {"names":names,"marks":marks,"grade":grades}
>>> students
{'names': ['Ram', 'Shyam', 'Goapl', 'Rohan'], 'marks': [56, 67, 65, 87], 'grade': ['b', 'b+', 'b+', 'a']}
>>> 
