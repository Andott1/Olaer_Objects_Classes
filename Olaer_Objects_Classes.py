import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * self.radius ** 2
        print(f"Area of the circle: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle: {circle_perimeter:.2f}")


while True:
    try:
        radius_value = float(input("Enter the radius of the circle: "))
        if radius_value <= 0:
            print("Radius must be a positive number\n")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.\n")

my_circle = Circle(radius_value)

my_circle.area()
my_circle.perimeter()
