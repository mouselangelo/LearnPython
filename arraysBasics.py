# arrays can contain mixed elements
# Questiion: array vs list?
mixed = [1, "two", 3.1, {"first_name": "John", "last_name": "Doe"}]
print(mixed)

# define using 'range'
numbers = range(10)

# access by index, including -1 (starts from end)
print(numbers[1]) # second element
print(numbers[-2]) # second from end

# access by "range" fromIndex:toIndex
print(numbers[:]) # defaults to all elements
print(numbers[1:5]) # index 1 is included, 5 is not
print(numbers[-5:-1]) # negatives ok (to should be "higher")
# can also specify a "step" i.e. fromIndex:toIndex:step
print(numbers[::1]) # every element
print(numbers[::2]) # every 2nd element
print(numbers[1::2]) # every 2nd element, starting from 1

print(numbers[::-1]) # reverse order
print(numbers[5:2:-1]) # reverse order, starting from index 5, up to index 2

numbers.append(1) # add to end
print(numbers[-1])

numbers.insert(5, "not a number") # insert value at index 5
print(numbers[3:7])

numbers[5] = 1 # assign value by index
print(numbers[3:7])

print(numbers.count(1)) # count of '1' in numbers (not count of list)
