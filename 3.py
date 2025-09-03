class Animal:

    def bark(self):
        print('Animal is barking')

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} is barking"

d = Dog("Rex")
print(d.name)
print(d.bark())                    