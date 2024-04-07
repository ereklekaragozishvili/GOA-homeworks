def arithmetic_mean(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)

my_numbers = [1, 2, 3, 4, 5]
mean = arithmetic_mean(my_numbers)
print(mean)  