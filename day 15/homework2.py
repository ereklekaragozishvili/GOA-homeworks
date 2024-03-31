correct_password = "Goa best"
incorrect_attempts = 0

while True:
    user_password = input("Enter the password: ")

    if user_password == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        incorrect_attempts += 1
        print("Incorrect password. Please try again.")
        print(f"Number of incorrect attempts: {incorrect_attempts}")