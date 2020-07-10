from mammal import Mammal


def print_all_cats():
    print("************************* CATS: ***************************\n")
    for i, cat in enumerate(Cat.catList):
        print(i+1, " cat:", "\nname:", cat.get_name(), "\nage:", cat.get_age(),
              "\ngender:", cat.get_gender(), "\nweight:", cat.get_weight(),
              "\nbreed:", cat.get_cat_breed(),
              "\nis hungry?:", cat.get_is_hungry(), "\nis need a vet visit?: ", cat.get_is_need_a_vet(), sep=' ')


def print_cat_info(cat):
    print("************************* DOG: ***************************\n")
    print(" Cat:", "\nname:", cat.get_name(), "\nage:", cat.get_age(), "\ngender:",
          cat.get_gender(), "\nweight:", cat.get_weight(), "\nbreed:", cat.get_cat_breed(),
          "\nis hungry?:", cat.get_is_hungry(), "\nis need a vet visit?: ", cat.get_is_need_a_vet(), sep=' ')


def if_anyone_cat_is_hungry():
    print("***************List of hungry cats:***************")
    for cat in Cat.catList:
        if cat.get_is_hungry() != 'no':
            print_cat_info(cat)
            choice = input('Do you want feed them now? yes/no')
            if choice == 'yes':
                cat.set_is_hungry('no')
                print("Cat ", cat.get_name(), " is not hungry anymore")
    input()


def if_anyone_cat_need_go_to_vet():
    print("***************List of dogs who should go to vet:***************")
    for cat in Cat.dogList:
        if cat.get_is_need_a_vet() != 'no':
            print_cat_info(cat)
            choice = input('Do you want go to the vet  now? yes/no')
            if choice == 'yes':
                cat.set_is_need_a_vet('no')
                print("Cat ", cat.get_name(), "is not need vet anymore")
        input()


def if_anyone_cat_need_go_to_vet():
    print("***************List of cats who should go to vet:***************")
    for cat in Cat.catList:
        if cat.get_is_need_a_vet() != 'no':
            print_cat_info(cat)
    input()


class Cat(Mammal):
    catList = []

    def __init__(self, name, age, weight, gender, is_hungry, is_need_a_vet, cat_breed):
        super().__init__(name, age, weight, gender, is_hungry, is_need_a_vet)
        self.__cat_breed = cat_breed
        Cat.catList.append(self)

    def set_cat_breed(self, cat_breed):
        self.__cat_breed = cat_breed

    def get_cat_breed(self):
        return self.__cat_breed


