from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, r):
        self.r = r


    def area(self):
        print(3.14 * (self.r**2))

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
     
    def area(self):
        print(self.a * self.b)

c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())