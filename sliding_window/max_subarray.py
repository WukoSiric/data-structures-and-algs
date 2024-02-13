import random 
import math 

def find_max_subarray(array: list[int], window_size: int) -> int: 
    maximum = -math.inf
    current_running_sum = 0 
    for i in range(len(array)): 
        current_running_sum += array[i] 
        if i >= window_size - 1: 
            maximum = max(maximum, current_running_sum)
            current_running_sum -= array[i - (window_size - 1)]
    return maximum

def main(): 
    array = []
    for i in range(8): 
        array.append(random.randint(1, 10))
    print(array)
    print(find_max_subarray(array, 3))

if __name__ == "__main__": 
    main()