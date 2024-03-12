def increasing_stack(array: list[int]) -> list[int]:
	stack = []
	stack.append(array[0])
	for i in range(1, len(array)):
		while stack and stack[-1] > array[i]: 
			stack.pop()
		stack.append(array[i])
		print(stack)
	return stack 

def main(): 
	array = [3, 8, 4, 9, 13, 6]
	result = increasing_stack(array)
	print(result)
	pass

if __name__ == "__main__": 
	main()