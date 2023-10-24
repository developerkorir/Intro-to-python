"""
It is used to generate a range of numbers
"""
# range of numbers 0-6 excluding 6
numbers = range(6)
# iterate through the range and print
for x in numbers:
    print(x)

# range of numbers between 6-13 excluding 13
numbers2 = range(6, 13)
for x in numbers2:
    print(x)

# print a range with a step
# value is incremented by 2 (step)
numbers3 = range(5, 20, 2)
for x in numbers3:
    print(x)
