Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "ram@gmail.com"
>>> text = "hello this is Ram"
>>> import re
>>> re.match(/[A-Z]/,text)
SyntaxError: invalid syntax
>>> re.match(\[A-Z]\,text)
SyntaxError: unexpected character after line continuation character
>>> re.match('[A-Z]',text)
>>> re.match('[A-Z]\w+',text)
>>> re.match('\[A-Z]\w+\',text)
	 
SyntaxError: EOL while scanning string literal
>>> re.match('/[A-Z]\w+/',text)
>>> re.search('/[A-Z]\w+/',text)
>>> re.search('[A-Z]\w+',text)
<re.Match object; span=(14, 17), match='Ram'>
>>> re.search('[A-Z]',text)
<re.Match object; span=(14, 15), match='R'>
>>> re.search('[A-Z]\w',text)
<re.Match object; span=(14, 16), match='Ra'>
>>> re.search('[A-Z]\w+',text)
<re.Match object; span=(14, 17), match='Ram'>
>>> re.findall('[A-Z]\w+',text)
['Ram']
>>> re.match('[A-Z]\w+',text)
>>> x = "hello this is ram and email id is ram@gmail.com"
>>> re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+',text)
[]
>>> re.findall('[a-z]\w+[@]\w+[.]\w+',text)
[]
>>> re.findall('([a-z]\w)+([@]\w)+[.]\w+',text)
[]
>>> re.findall('[a-z]\w+[@]',text)
[]
>>> re.findall('[a-z]\w[@]',text)
[]
>>> re.findall('[a-z]+[@]',text)
[]
>>> re.findall('[a-z]+\w[@]',text)
[]
>>> re.findall('[a-z]\w[@]',x)
['am@']
>>> re.findall('[a-z]\w+[@]\w+[.]\w+',x)
['ram@gmail.com']
>>> re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+',x)
[' ram@gmail.com']
>>> x = "hello this is ram and email id is ram@gmail.com and shyam is 12shyam_12@gmail.com"
>>> re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+',x)
[' ram@gmail.com', ' 12shyam_12@gmail.com']
>>> re.match('[A-Z]\w+',text)
>>> re.match([A-Z]\w+,text)
SyntaxError: unexpected character after line continuation character
>>> re.match(/[A-Z]\w+/,text)
SyntaxError: invalid syntax
>>> re.match('/[A-Z]\w+/',text)
>>> if re.match('[A-Z]\w+', text):
	print("Found")
else:
	print("Not Found")

	
Not Found
>>> if re.search('[A-Z]\w+', text):
	print("Found")
else:
	print("Not Found")

	
Found
>>> re.match("[A-Z]\w+",text)
>>> 
