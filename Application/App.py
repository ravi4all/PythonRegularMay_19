import readWriteData

users = []

def login():
    print('You are in login fn..')
    email = input('Enter email: ')
    password = input('Enter password: ')
    userInput = {'email':email, 'password': password}
    '''for i in range(len(users)):
        print(users[i])
        if userInput['email'] == users[i]['email'] and
        userInput['password'] == users[i]['password']:
            print('Login successful')
        else:
            print('Login failed')'''
    for user in users:
        print(user)
        if userInput['email'] == user['email'] and \
        userInput['password'] == user['password']:
            print('Login successful')
        else:
            print('Login failed')

def register():
    print('You are in register fn..')
    name = input('Enter name: ')
    email = input('Enter email: ')
    password = input('Enter password: ')
    user = {'name':name, 'email':email, 'password':password}
    users.append(user)
    print(users)
    print('Registration successful')
    readWriteData.writeUser(user)

def errorHandler():
    print('Invalid choice..')

while True:
    print('''
    1. Login
    2. Register
    3. Exit
    ''')
    ch = input('Enter your choice: ')
    options = {'1':login, '2':register, '3':quit}
    x = options.get(ch,errorHandler)
    x()
#options[ch]

