numbers = []
numbers.append(1)
numbers.append(3)
numbers.append(5)
numbers.append(7)

## stack-like operations
print(numbers)
numbers.pop()
print(numbers)
numbers.append(10)
print(numbers.pop())

##queue-like operations
print(numbers)
numbers.pop(0)
print(numbers)
numbers.pop(0)
print(numbers)

