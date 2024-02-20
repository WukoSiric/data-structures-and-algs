# Python only supports recursing up to 996 steps
# Calling walk(1000) throws an error

def walk(steps: int) -> None: 

    if steps <= 0: 
        return

    walk(steps - 1)
    print("Walked this many steps: " + str(steps))
    pass



walk(100)