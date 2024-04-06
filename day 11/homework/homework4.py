pin = 543543

user_pin = int(input("enter a pin code: "))

if user_pin == pin:
    print("Withdrawal (1)")
    print("Deposit (2)")
    print("Balance (3)")
else:
    print("access denied!")