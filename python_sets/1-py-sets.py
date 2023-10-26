# Set Size and Membership
# The len() function returns the number of elements in a set
x = {'foo', 'bar', 'baz'}
len(x)
# print(len(x))

# Operating on a Set
# Unions of sets

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

# The union of x1 and x2 is a set consisting of all elements in either set.
print(x1 | x2)
# OR
# using .union() method
print(x1.union(x2))
# x1.union(x2) and x1 | x2 both return the set of all elements in either x1 or x2

print(x1.intersection(x2))
