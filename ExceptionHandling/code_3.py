def atm():
    total = 5000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        raise ValueError("Login Failed...")

    amount = int(input("Enter the amount : "))
    if amount > total:
        raise ValueError("Insufficient Balance")
    else:
        total -= amount
        print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)
