class Flyer:

    def fly(self):
        pass

class Swimmer:

    def swim(self):
        pass

class Duck(Flyer, Swimmer):

    def fly(self):
        print('Duck is flying')

        
    def swim(self):
        print('Duck is swimming')

duck = Duck()
duck.fly()
duck.swim()