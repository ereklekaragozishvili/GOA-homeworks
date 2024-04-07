def sum_of_numbers(numbers):
    result = 0

    for num in numbers:
        if num > 10:
            result = result + num
    
    return result

print(sum_of_numbers([1,2,3,11,15,5]))
