#Abbreviate a Two Word Name
def abbrev_name(name):
    name = name.upper()
    splited_name = name.split(" ")
    
    firstname = splited_name[0]
    lastname = splited_name[1]
    
    result = firstname[0] + "." + lastname[0]
    
    return result

print(abbrev_name("erekle karagozishvili"))

