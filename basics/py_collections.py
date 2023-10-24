# lists, dictionary, set, tuple

cities = ["Nairobi", "Nakuru", "Eldoret", "Kigali", "Arusha"]

# dictionary
# key: value
# uses curly braces
car = {
    "Car": "BMW",
    "model": "M3",
    "year": 2020,
    "transmission": "manual",
    "color": "white",
    "owners": ["Calton", "Korir"]
}

# set - data that does not repeat
friends = {"Mike", "Walter", "John", "Mike", "John"}  # unique elements
print(friends)

# Tuples
# cannot be change programmatically
workers = ("Jane", "June", "Jann")  # immutable

print(cities)
print(car)
print(workers)

print(car["model"])

for key, value in car.items():
    print(key, " : ", value)
