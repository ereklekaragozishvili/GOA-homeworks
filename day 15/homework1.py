def check_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is not even. The next even number is {number + 1}.")


user_input = input("Enter a number: ")


try:
    user_number = int(user_input)
    check_even(user_number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")