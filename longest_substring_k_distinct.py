import math

def longest_substring_length(string: str, distinct_char_count: int) -> int: 
    max_substring_length = 0
    current_max = 0 
    substring_letters = set()
    for i in range(len(string)): 
        max_substring_length = max(current_max, max_substring_length)
        substring_letters.add(string[i])
        current_max += 1

        # shirinking functionality
        while len(substring_letters) < distinct_char_count:
            pass

def main():
    pass

if __name__ == "__main__":
    main() 