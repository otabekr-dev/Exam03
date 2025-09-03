class Temperature:

    def __init__(self, temperature) -> float:
        self.temperature = temperature

    @property
    def celcius(self) -> float:
        return self.temperature

    @property
    def farenheit(self) -> float:
        return (self.temperature + 32)

t = Temperature(0)
print(t.celcius)           
print(t.farenheit)           