def reverse_string(string : str) -> str: 
    # base case
    if len(string) <= 1: 
        return string
    
    # recursive case, if length is greater than 1
    return reverse_string(string[1:]) + string[0]

user_string = str(input())

print("Reversed string: ")
print(reverse_string(user_string))