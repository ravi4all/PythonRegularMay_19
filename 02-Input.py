# by default input takes string type of data
name = input("Enter your name : ")
msg = "Hello {}".format(name)
print(msg)

# Multiline Print
print("""
            Welcome to python programming :
        1. Add
        2. Sub
        3. Div
        4. Mul
""")

# so we need to type cast/convert the input into int
f_num = int(input("Enter first number : "))
s_num = int(input("Enter second number : "))
result = f_num + s_num
print(result)
