def get_prefix_sum_array(array: list[str]): 
    prefix_array = list()

    for i in range(len(array)): 
        if i == 0: 
            prefix_array.append(array[0])
        else: 
            prefix_array.append(array[i] + prefix_array[i-1])
    return prefix_array


def main():
    sample_array = [1, 2, 80, 100]
    print(sample_array)
    print(get_prefix_sum_array(sample_array))

if __name__ == "__main__": 
    main()
