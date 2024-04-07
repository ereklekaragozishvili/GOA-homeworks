def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in inputStr:
        if i in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1
        else:
            pass
    return num_vowels