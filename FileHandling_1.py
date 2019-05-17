file = open('file_1.txt','r')
#data = file.read()

#data = file.read(10)
#file.seek(10)
#data = file.read()

#data = file.readlines()
data = file.readline()
print(data)
file.close()
