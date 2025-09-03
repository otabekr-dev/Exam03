class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade} course"


s = Student("Ali", 20, 2)
print(s.introduce())