name = "Carlton"
city = "Nairobi"

# Numbers
age = 23
weight = 69

# concatenate strings
print(name+city)

print(name+" "+city)
# Duplicate strings
print(name*4)

# print(name+age)

print(f"I am {name}, I am {age} years and I live in {city}, I weigh {weight} KGs")

# Methods associated with string object
sentence = "These are python functions to do with strings."
# print the sentence in uppercase followed by the original
# the value can still be stored in a variable
print(sentence.upper(), sentence)
# Length of a sentence
print(len(sentence))
print(sentence.capitalize())

# .strip() removes white space at the beginning of a string

# replacing section of the string
print(sentence.replace("functions", "methods"))
# methods/functions can be chained
print(sentence.replace("functions", "methods").upper())  # chaining

