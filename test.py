
class Circle:
    # variable 
    num_circles = 0

    # Constructor
    def __init__(self, radius):
        self.radius = radius
        Circle.num_circles += 1

    # Calculate the area of the circle
    def area(self):
        return 3.14159 * self.radius ** 2  # Using pi as approximately 3.14159

    # Calculate the perimeter of the circle
    def perimeter(self):
        return 2 * 3.14159 * self.radius

    # Getter 
    def get_nbr_of_circles():
        return Circle.num_circles


# Test program
circle1 = Circle(8)
circle2 = Circle(5)

print("Circle 1")
print("\tArea      =", round(circle1.area(), 4))
print("\tPerimeter =", round(circle1.perimeter(), 4))    
  

print("Circle 2")
print("\tArea      =", round(circle2.area(), 4))
print("\tPerimeter =", round(circle2.perimeter(), 4))

print("\nNumber of circles =", Circle.get_nbr_of_circles())  

    
