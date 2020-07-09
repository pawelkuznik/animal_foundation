from animal import Animal

class Mammal(Animal):
    def __init__(self, name, age, weight, gender, is_hungry, is_need_a_vet):
        super().__init__(name, age, weight, gender, is_hungry, is_need_a_vet)

