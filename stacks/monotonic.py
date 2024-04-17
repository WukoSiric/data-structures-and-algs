def increasing_stack(array: list[int]) -> list[int]:
	stack = []
	stack.append(array[0])
	for i in range(1, len(array)):
		while stack and stack[-1] > array[i]: 
			stack.pop()
		stack.append(array[i])
		print(stack)
	return stack 

def get_next_greater_indexes(array: list[int]) -> list[int]: 
	stack = [] 
	next_greater_indexes = [-1 for i in range(len(array))]

	for i in range(len(array)): 
		while(len(stack) and array[i] > array[stack[-1]]): 
			stack_top = stack.pop()
			next_greater_indexes[stack_top] = i

		stack.append(i)
	return next_greater_indexes

def main(): 
	array = [3, 8, 4, 9, 13, 6]
	result = get_next_greater_indexes(array)
	print(result)
	pass

if __name__ == "__main__": 
	main()