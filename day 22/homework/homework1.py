#1
def number_to_string(num):
    return str(num)

#2
def solution(string):
    return string[::-1]

#3
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return  "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return  "Player 1 won!"
    else:
        return "Player 2 won!"


#4 
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

#5
def square_sum(numbers):
    result = []
    for i in numbers:
        i = i ** 2
        result.append(i)
    return sum(result)

