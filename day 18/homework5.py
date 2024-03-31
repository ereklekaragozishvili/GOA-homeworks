def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

user_input = input("Enter a word: ")
reversed_result = reverse_word(user_input)
print("Reversed word:", reversed_result)