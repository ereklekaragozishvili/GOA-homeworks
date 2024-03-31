def reverse_word(word):
    reversed_word = ""
    for i in range(len(word)):
        reversed_word = word[i] + reversed_word
    return reversed_word

def main():
    user_input = input("Enter a word: ")
    reversed_result = reverse_word(user_input)
    print("Reversed word:", reversed_result)

main()