def filter_list(strings_list):
    filtered_list = 0

    for word in strings_list:
        if word [0]== 'a':
         filter_list.append(word)
    return filtered_list

words = ["apple", "avalanche","analizi","meat","water","chicken"]


print(filter_list(words))
