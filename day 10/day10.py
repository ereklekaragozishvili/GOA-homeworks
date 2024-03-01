password = 1234 
authorized = False

while authorized != True:
    user_login = int(input("Enter password!"))

    if user_login == password:
        print("Access Granted")
        authorized == True
    else:
        print("try Again!!")