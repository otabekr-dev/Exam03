import json

class JsonMixin:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "price": self.price
        })


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


p = Product("Laptop", 1500)
print(p.to_json())
