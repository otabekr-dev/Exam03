class BankAccount:
     
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else: 
            raise(ValueError('Manfiy raqam kiritdingiz'))

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise(ValueError('Bank hisobingizda bunday miqdor mavjud emas'))

    def get_balance(self):
        return self.__balance


acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())

