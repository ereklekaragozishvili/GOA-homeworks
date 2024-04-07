def filter_arr(start_num,end_num):
    numbers=[]
    filtered_list=[]
    for i in range(start_num,end_num):
        numbers.append(i)
        print(numbers)
        for i in numbers:
            if i % 2 == 0:
                filtered_list.append(i**2)
            else:
                filtered_list.append(i**0.5)
                return filtered_list

start_num = int(input("please enter your first number: "))
end_num = int(input("please enter your second number"))
result_list = filter_arr(start_num,end_num)
print(result_list)