# Faster way because it modifies the list in place
numbers = [4,9,7,5,1,3,2]
numbers.sort()
print(numbers)

# Slower way because it builds a new sorted list
numbers = [4,9,7,5,1,3,2]
ordered_numbers = sorted(numbers)
print(ordered_numbers)