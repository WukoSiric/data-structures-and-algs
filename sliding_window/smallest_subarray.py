import math

def smallest_subarray_size(target_value: int, array: list[int]) -> int: 
    window_start = 0
    current_window_sum = 0
    smallest_size = math.inf
    for window_end in range(len(array)): 
        current_window_sum += array[window_end]
        while current_window_sum >= target_value: 
            smallest_size = min(smallest_size, window_end - window_start + 1)
            current_window_sum -= array[window_start]
            window_start += 1
    return smallest_size

def main(): 
    array = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    target_sum = 8
    print(smallest_subarray_size(target_sum, array))

if __name__ == "__main__":
    main()