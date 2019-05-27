def atm():
    total = 5000
    pin = input("Enter your PIN : ")
    assert(pin == "1234"), "Login Failed"
    print("Login Success")

    amount = int(input("Enter the amount : "))
    assert(amount > total), "Insufficient Balance"
    total -= amount
    print("Remaining balance is",total)

try:
    atm()
except AssertionError as err:
    print(err)
