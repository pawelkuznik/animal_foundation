from mammal import Mammal


def print_all_dogs():
    print("************************* DOGS: ***************************\n")
    for i, dog in enumerate(Dog.dogList):
        print(i+1, " Dog:", "\nname:", dog.get_name(), "\nage:", dog.get_age(),
              "\ngender:", dog.get_gender(), "\nweight:", dog.get_weight(),
              "\nbreed:", dog.get_dog_breed(),
              "\nis hungry?:", dog.get_is_hungry(), "\nis need a vet visit?: ", dog.get_is_need_a_vet(), sep=' ')


def if_anyone_dog_is_hungry():
    print("***************List of hungry dogs:***************")
    for dog in Dog.dogList:
        if dog.get_is_hungry() != 'no':
            print_dog_info(dog)
            choice = input('Do you want feed them now? yes/no')
            if choice == 'yes':
                dog.set_is_hungry('no')
                print("Dog ", dog.get_name(), "not hungry anymore")
    input()


def if_anyone_dog_need_go_to_vet():
    print("***************List of dogs who should go to vet:***************")
    for dog in Dog.dogList:
        if dog.get_is_need_a_vet() != 'no':
            print_dog_info(dog)
            choice = input('Do you want go to the vet  now? yes/no')
            if choice == 'yes':
                dog.set_is_need_a_vet('no')
                print("Dog ", dog.get_name(), "is not need vet anymore")
        input()



def print_dog_info(dog):
    print("************************* DOG: ***************************\n")
    print(" Dog:", "\nname:", dog.get_name(), "\nage:", dog.get_age(), "\ngender:",
          dog.get_gender(), "\nweight:", dog.get_weight(), "\nbreed:", dog.get_dog_breed(),
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
