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

# BMI calculator
height = 1.73
weight = 60

bmi = weight / height ** 2
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")

sentence = "Kenya, Uganda and Tanzania"

if "kenya" in sentence.lower():
    print("Yes, it exists")
else:
    print("Does not exist")
