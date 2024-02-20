def factorial(number: int) -> int: 
    if number <= 1: 
        return 1
    
    return number * factorial(number - 1)

def main(): 
    print(factorial(5))

if __name__ == "__main__": 
    main() 