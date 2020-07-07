from mammal import Mammal

class Cat(Mammal):
    def __init__(self, cat_breed):
        self.cat_breed = cat_breed
        super().__init__('Cat')


