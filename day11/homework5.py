username = "admin"
password = "password123"


username_input = input ("Enter your username: ")
password_input = input ("Enter a password: ")


if username_input == username and password_input == password:
    print("Login successful!")
else:
    print("Access denied!")
