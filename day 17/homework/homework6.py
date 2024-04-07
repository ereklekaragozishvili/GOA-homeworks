def strings_length(strings_list):
    length_list = []

    for word in strings_list:
        length_list.append(len(word))
    
    return length_list

print(strings_length(["qishvardi","anzori","saba","jemali"]))