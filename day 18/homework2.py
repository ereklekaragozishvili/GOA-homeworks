def add_names_to_list():
    name_list = []
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    name_list.append(first_name)
    name_list.append(last_name)
    
    
    return name_list


result_list = add_names_to_list()
print("Updated list:", result_list)