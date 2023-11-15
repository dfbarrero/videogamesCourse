
def fib(n):
    a, b = 0, 1
    while a < n:
	    print(a, end= ' ')
	    a, b = b, a+b

    print()

def fib2(n):
    result = [] # Declare a new list
	a, b = 0, 1
    while a < n:
	    result.append(a) # Add to the list
	    a, b = b, a+b
    return result
