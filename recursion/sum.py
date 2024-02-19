def findSum(nums: list[int]):
    # base case
    if len(nums) <= 1: 
        return nums[0]

    return nums[0] + findSum(nums[1:])


def findIntSum(number: int): 
    number = str(number)

    if len(number) <= 1: 
        return int(number)
    
    return int(number[0]) + findIntSum(int(number[1:]))


def main(): 
    array = [1, 4, 5, 6]
    print(findSum(array))
    print(findIntSum(45))

if __name__ == "__main__": 
    main()