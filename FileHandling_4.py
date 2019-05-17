file = open('C:/Users/asus/Documents/794250_science_512x512.png','rb')
data = file.read()
#print(data)
file.close()

file = open('img_1.png','wb')
file.write(data)
file.close()
