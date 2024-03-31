num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
start = min(num1, num2)
end = max(num1, num2)
print("Multiples of five between", start, "and", end, "inclusive:")
for num in range(start, end + 1):
    if num % 5 == 0:
        print(num)