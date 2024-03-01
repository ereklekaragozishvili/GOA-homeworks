age = int(input("enter your age:"))

if 0 > age < 12:
    print('child')
elif age < 19:
    print('teenager')
elif age > 19:
    print('adult')
else:
    print("what are u??!!")