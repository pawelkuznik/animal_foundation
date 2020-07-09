from mammal import Mammal


def print_all_dogs():
    print("************************* DOGS: ***************************\n")
    for i, dog in enumerate(Dog.dogList):
        print(i+1, " Dog:", "\nname:", dog.get_name(), "\nage:", dog.get_age(),
              "\ngender:", dog.get_gender(), "\nweight:", dog.get_weight(),
              "\nbreed:", dog.get_dog_breed(),
              "\nis hungry?:", dog.get_is_hungry(), "\nis need a vet visit?: ", dog.get_is_need_a_vet(), sep=' ')


class Dog(Mammal):
    dogList = []

    def __init__(self, name, age, weight, gender, is_hungry, is_need_a_vet, dog_breed):
        super().__init__(name, age, weight, gender, is_hungry, is_need_a_vet)
        self.__dog_breed = dog_breed
        Dog.dogList.append(self)

    def set_dog_breed(self, dog_breed):
        self.__dog_breed = dog_breed

    def get_dog_breed(self):
        return self.__dog_breed
