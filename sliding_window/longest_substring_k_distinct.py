import math

def longest_substring_length(string: str, distinct_char_count: int) -> int: 
    max_substring_length = 0
    window_start = 0
    substring_letters = {}
    for i in range(len(string)): 
        substring_letters[string[i]] = 1 + substring_letters.get(string[i], 0)

        # shirinking functionality
        while len(substring_letters) > distinct_char_count:
            # remove the element at the window_start from the hash
            substring_letters[string[window_start]] -= 1

            # if the element is now == 0, completely remove from the hashmap 
            if substring_letters[string[window_start]] == 0: 
                substring_letters.pop(string[window_start])   

            # incremeent window_start 
            window_start += 1
        if sum(substring_letters.values()) > max_substring_length: 
            max_substring_length = sum(substring_letters.values())
    return max_substring_length

def main():
    random_string = "AAAHHIBC"
    print(longest_substring_length(random_string, 2))
    random_string = "AAAHHIBC"
    print(longest_substring_length(random_string, 3))
    random_string = "AAAHHIBC"
    print(longest_substring_length(random_string, 4))
    random_string = "AAAHHIBC"
    print(longest_substring_length(random_string, 5))


if __name__ == "__main__":
    main() 