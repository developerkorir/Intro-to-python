"""
Lists are objects
They have methods available for them
A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
"""

# List of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)
# add element to end of the list
numbers.append(6)
print(numbers)
# inserting an element at a particular index
# add 0 to index 0
numbers.insert(0, 0)
print(numbers)
# remove an object from a list
numbers.remove(4)
print(numbers)

# remove all objects in a list
# .clear method takes in no parameters
"""
numbers.clear()
print(numbers)
"""

# Check for availability of object in a list
# Result is a boolean
# result is a false since we removed 4 earlier
print(4 in numbers)

# number of elements in a list
# len is a built-in function that returns length of an object
print(len(numbers))
