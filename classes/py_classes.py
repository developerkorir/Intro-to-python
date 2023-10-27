class Circle:
    def __init__(self, radius):  # constructor
        self.circle_radius = radius

    def calc_area(self):
        a = 22 / 7 * self.circle_radius ** 2
        print(f"Area id {round(a)}")

    def circle_perimeter(self):
        p = 22 / 7 * self.circle_radius * 2
        print(f"Circumference is {round(p)}")


# objects
c1 = Circle(10)
c2 = Circle(14)
c3 = Circle(13.25)

c1.circle_perimeter()
c1.calc_area()

c2.calc_area()
