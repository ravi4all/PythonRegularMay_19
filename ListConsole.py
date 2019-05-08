Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = ['Ram','Shyam','Gopal','Sumit','Ramesh',23,43,32,45,43]
>>> type(x)
<class 'list'>
>>> x[0]
'Ram'
>>> x[-1]
43
>>> x[0:5]
['Ram', 'Shyam', 'Gopal', 'Sumit', 'Ramesh']
>>> x[0:]
['Ram', 'Shyam', 'Gopal', 'Sumit', 'Ramesh', 23, 43, 32, 45, 43]
>>> x[:5]
['Ram', 'Shyam', 'Gopal', 'Sumit', 'Ramesh']
>>> x[:]
['Ram', 'Shyam', 'Gopal', 'Sumit', 'Ramesh', 23, 43, 32, 45, 43]
>>> x[:-1]
['Ram', 'Shyam', 'Gopal', 'Sumit', 'Ramesh', 23, 43, 32, 45]
>>> x[10:1]
[]
>>> x[10:1:-1]
[43, 45, 32, 43, 23, 'Ramesh', 'Sumit', 'Gopal']
>>> x[::-1]
[43, 45, 32, 43, 23, 'Ramesh', 'Sumit', 'Gopal', 'Shyam', 'Ram']
>>> x = []
>>> x.append(2)
>>> x
[2]
>>> x.append(10)
>>> x
[2, 10]
>>> x.append(12)
>>> x.append(121)
>>> x.append(21)
>>> x.append(23)
>>> x.append(3)
>>> x.append(16)
>>> x.append(61)
>>> x
[2, 10, 12, 121, 21, 23, 3, 16, 61]
>>> x.pop()
61
>>> x
[2, 10, 12, 121, 21, 23, 3, 16]
>>> x.insert(2,4)
>>> x
[2, 10, 4, 12, 121, 21, 23, 3, 16]
>>> x.pop(5)
21
>>> x = []
>>> for i in range(101):
	if i % 2 != 0:
		x.append(i)

		
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> y = []
>>> for i in range(101):
	if i % 2 == 0:
		y.append(i)

		
>>> y
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> x + y
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> x.extend(y)
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> x.sort()
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> x.sort(reverse=True)
>>> x
[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x.index(4)
96
>>> x = [43, 45, 32, 43, 23, 'Ramesh', 'Sumit', 'Gopal', 'Shyam', 'Ram']
>>> x.remove(4)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x.remove(4)
ValueError: list.remove(x): x not in list
>>> x.remove(45)
>>> x
[43, 32, 43, 23, 'Ramesh', 'Sumit', 'Gopal', 'Shyam', 'Ram']
>>> x.pop(4)
'Ramesh'
>>> x
[43, 32, 43, 23, 'Sumit', 'Gopal', 'Shyam', 'Ram']
>>> data = [['Ram','Shyam','Gopal','Anuj'],['TCS','HCL','IBM','TCS'],['IT','CS','HR','IT']]
>>> data[0]
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> data[1]
['TCS', 'HCL', 'IBM', 'TCS']
>>> data[2]
['IT', 'CS', 'HR', 'IT']
>>> data[0][2]
'Gopal'
>>> data[1][2]
'IBM'
>>> data[2][2]
'HR'
>>> for i in range(len(data[0])):
	print(data[0][i])

	
Ram
Shyam
Gopal
Anuj
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i])

	
Ram TCS
Shyam HCL
Gopal IBM
Anuj TCS
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i], data[2][i])

	
Ram TCS IT
Shyam HCL CS
Gopal IBM HR
Anuj TCS IT
>>> data
[['Ram', 'Shyam', 'Gopal', 'Anuj'], ['TCS', 'HCL', 'IBM', 'TCS'], ['IT', 'CS', 'HR', 'IT']]
>>> data = \['Ram', 'Shyam', 'Gopal', 'Anuj']
SyntaxError: unexpected character after line continuation character
>>> data = ['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> data[0] = 'Raman'
>>> data
['Raman', 'Shyam', 'Gopal', 'Anuj']
>>> x = data
>>> y = x
>>> data
['Raman', 'Shyam', 'Gopal', 'Anuj']
>>> x
['Raman', 'Shyam', 'Gopal', 'Anuj']
>>> y
['Raman', 'Shyam', 'Gopal', 'Anuj']
>>> x[0] = 'Ram'
>>> x
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> y
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> x = data[:]
>>> x = data
>>> x == data
True
>>> x == y
True
>>> y == data
True
>>> x = data[:]
>>> x == data
True
>>> x == y
True
>>> x is y
False
>>> x = data
>>> y = x
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> x
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> y
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> x == y == data
True
>>> x is data
True
>>> y is data
True
>>> x is y
True
'
>>> id(x)
2947062670024
>>> id(y)
2947062670024
>>> x = data[:]
>>> x
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj']
>>> x == data
True
>>> x is data
False
>>> data = ['Ram', 'Shyam', 'Gopal', 'Anuj',['TCS','HCL','IBM','HCL']]
>>> x = data[:]
>>> x[0] = 'Raman'
>>> x
['Raman', 'Shyam', 'Gopal', 'Anuj', ['TCS', 'HCL', 'IBM', 'HCL']]
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj', ['TCS', 'HCL', 'IBM', 'HCL']]
>>> x[-1]
['TCS', 'HCL', 'IBM', 'HCL']
>>> x[-1][0] = 'INFY'
>>> x
['Raman', 'Shyam', 'Gopal', 'Anuj', ['INFY', 'HCL', 'IBM', 'HCL']]
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj', ['INFY', 'HCL', 'IBM', 'HCL']]
>>> import copy
>>> y = copy.deepcopy(data)
>>> y
['Ram', 'Shyam', 'Gopal', 'Anuj', ['INFY', 'HCL', 'IBM', 'HCL']]
>>> y[-1][0] = 'TCS'
>>> y
['Ram', 'Shyam', 'Gopal', 'Anuj', ['TCS', 'HCL', 'IBM', 'HCL']]
>>> data
['Ram', 'Shyam', 'Gopal', 'Anuj', ['INFY', 'HCL', 'IBM', 'HCL']]
>>> x
['Raman', 'Shyam', 'Gopal', 'Anuj', ['INFY', 'HCL', 'IBM', 'HCL']]
>>> 
