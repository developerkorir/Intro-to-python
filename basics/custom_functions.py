def say_my_name():
    print("Welcome to M3")


say_my_name()


def say_my_name(name):  # name is a parameter/argument
    print(f"Hey, my name is {name}")


# say_my_name("Calton")


def calculate_volume_cylinder(radius, height):
    volume = 22 / 7 * radius ** 2 * height
    print(volume)
    return volume


# calculate_volume_cylinder(7,20)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    return total


# # add_numbers(10, 20, 30)
# v1 = calculate_volume_cylinder(13,22)
# print(round(v1))
