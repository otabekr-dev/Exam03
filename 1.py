class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def get_info(self):
        return f'{self.brand} {self.model} ({self.year})'


car = Car("BMW", "X5", 2020)
print(car.get_info())            