from mammal import Mammal

class Dog(Mammal):
    def __init__(self, name, age, weight, gender, dog_breed):
        super().__init__(name, age, weight, gender)
        self.dog_breed = dog_breed