data = "hello this is some data"
'''
file = open('file_2.txt', 'w')
file.write(data)
file.close()
'''

with open('file_2.txt','w') as file:
    file.write(data)
    data = file.read()

