Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world"
>>> type(text)
<class 'str'>
>>> len(text)
11
>>> text[0]
'h'
>>> text[5]
' '
>>> text[7]
'o'
>>> text[0:7]
'hello w'
>>> text[-1]
'd'
>>> text[8:1]
''
>>> text[8:1:-1]
'row oll'
>>> text[8::-1]
'row olleh'
>>> text[:]
'hello world'
>>> text[0:]
'hello world'
>>> text[:5]
'hello'
>>> text[0:10:2]
'hlowr'
>>> text[-1:-5]
''
>>> text[-1:-5:-1]
'dlro'
>>> text.capitalize()
'Hello world'
>>> text.title()
'Hello World'
>>> text.upper()
'HELLO WORLD'
>>> text.lower()
'hello world'
>>> text.find('o')
4
>>> text.count('o')
2
>>> text.find('o',5)
7
>>> text.center(10)
'hello world'
>>> text.center(12)
'hello world '
>>> text.center(13)
' hello world '
>>> text.center(40)
'              hello world               '
>>> text.center(40,'#')
'##############hello world###############'
>>> text.split()
['hello', 'world']
>>> text.islower()
True
>>> text.isupper()
False
>>> text.upper()
'HELLO WORLD'
>>> 
