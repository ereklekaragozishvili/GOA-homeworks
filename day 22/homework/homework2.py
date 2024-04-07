#1
def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
    	if i not in vowels:
        	new_string+= i 
			
#2
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))

#3
def get_middle(s):
    length = len(s) - 1 
    mid = length//2 
    if length % 2 == 0:
        return s[mid:mid+1]
    else:
        return s[mid:mid+2]
#4
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

#5
def find_short(s):
    return min(len(x) for x in s.split())
