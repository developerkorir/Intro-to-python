"""
Exercise 1
Create a program that converts weight
input by user to KG or Lbs
"""

weight = float(input("Weight: "))
weight_type = input("(K)g or (L)bs: ")

if weight_type.upper() == "L":
    # Convert pounds to KGs
    weight = weight / 2.20462
    print("Weight in Lbs: " + str(weight))
elif weight_type.upper() == "K":  # check both uppercase and lowercase
    # Convert KGs to Lbs
    weight = weight * 2.20462
    print("Weight in KG: " + str(weight))
