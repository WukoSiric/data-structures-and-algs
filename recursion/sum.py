def findSum(nums: list[int], sum):

    # base case
    if len(nums) <= 1: 
        return sum + nums[0]
    

    sum += nums[0]
    nums.pop(0)

    return findSum(nums, sum)


# findsum(array, 0)
# sum = 

def main(): 
    array = [1, 4, 5, 6]
    print(findSum(array, 0))

if __name__ == "__main__": 
    main()