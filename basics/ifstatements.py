"""
This is a multiline
comment in Python
Try it
"""

# This is a single line comment
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink some water")
elif temperature > 25:  # (10, 30]
    print("It's a nice day, let's code")
elif temperature > 10:  # (20, 30]
    print("It's a bit cold")
else:
    print("It's very cold")
