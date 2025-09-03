class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, obj2):
        aa = self.a + obj2.a
        bb = self.b + obj2.b
        return Vector(a = aa, b = bb)

    def __str__(self):
        return f"Vector({self.a}, {self.b})"
    
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)