def multipule_of_4(numbers):
    return[num for num in numbers if num % 4 == 0]
numbers_from_1_to_20=list(range(1,21))
filtered_list = multipule_of_4(numbers_from_1_to_20)
print(filtered_list)