def buildMonostack(array: list[int]) -> list[int]: 
    # initialize empty stack
    stack = [] 

    # iterate through all elements in array
    for i in range(len(array)): 
        while stack and stack[-1] > array[i]: 
            stackTop = stack.pop()

            # do something with stack top here
        
        if stack: 
            # do something with stack top here 
            pass
        
        stack.push()