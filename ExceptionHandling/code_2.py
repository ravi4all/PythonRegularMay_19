import io
try:
    file = open('file_1.txt','w')
    data = "hello this is python"
    file.write(data)

    data = file.read()
    print(data)
except io.UnsupportedOperation:
    print("File opened in different mode...")
finally:
    print("Finally executed...")
    file.close()
