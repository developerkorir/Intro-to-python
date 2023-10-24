"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary
"""
# A list of names
names = ["Fyog", "Yats", "Pikeman", "Chebet", "Moyo"]
# print name stored at index 0
print(names[0])
# Updating elements in a list
names[1] = "Ratty"
print(names)
# Select a range of values e.g. first three elements
# The element in the last index is ignored
# 0:3 is a range
print(names[0:3])
