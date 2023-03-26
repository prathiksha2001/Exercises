class Circle:
    def __init__(self,radius):
        self.radius = radius
    def computeArea(self):
        return 3.14 * self.radius * self.radius

obj = Circle(5)
print(obj.computeArea())

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculateArea(self):
        return self.length * self.breadth
    
obj1 = Rectangle(5,2)
print(obj1.calculateArea())