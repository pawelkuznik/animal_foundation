from animal import Animal

class Mammal(Animal):
    def __init__(self, name, age, weight, gender):
        super().__init__(name, age, weight, gender)

