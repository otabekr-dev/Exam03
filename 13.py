from abc import ABC, abstractmethod

class Payment:

    @abstractmethod
    def pay(self):
        pass

class PayPalPayment(Payment):

    def pay(self, amount):
        return f'Paid {amount} using Paypal'

class CardPayment(Payment):

    def pay(self, amount):
        return f'Paid {amount} using Card'

p1 = PayPalPayment()
p2 = CardPayment()
print(p1.pay(100))
print(p2.pay(200))        

