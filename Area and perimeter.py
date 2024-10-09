class Circle:

    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.141 * (self.radius**2)

    def perimeter(self):
        return 2 * 3.141 * self.radius


radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

print("Area:", circle.area())
print("Perimeter:", circle.perimeter())