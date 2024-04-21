class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): 
            low = i + 1 
            high = len(numbers) - 1

            while(low <= high): 
                mid = (low + high) // 2

                # check if found the value 
                if target == numbers[i] + numbers[mid]: 
                    return [i + 1, mid + 1]
                
                # answer could be in bottom half of array
                if target < numbers[i] + numbers[mid]: 
                    high = mid - 1

                # answer could be in top half of array
                elif target > numbers[i] + numbers[mid]:
                    low = mid + 1
        return 


