def is_palindrome(string: str) -> bool: 
    if len(string) <= 1: 
        return True
    
    if string[0] != string[-1]: 
        return False 
    
    string = string[1:-1]
    return is_palindrome(string)


def main(): 

    print("Enter the string to test: ")
    input_string = str(input())
    result = is_palindrome(input_string.upper())

    print()
    
    if result: 
        print(input_string + " is a palindrome!")
        return
    print(input_string + " is NOT a palindrome!")
    return

if __name__ == "__main__":
    main()