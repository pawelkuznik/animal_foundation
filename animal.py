class Animal(object):
    def __init__(self, name, age, weight, gender, is_hungry, is_need_a_vet):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__gender = gender
        self.__is_hungry = is_hungry
        self.__is_need_a_vet = is_need_a_vet

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self. __weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__weight = gender

    def get_is_hungry(self):
        return self.__is_hungry

    def set_is_hungry(self, is_hungry):
        self.__is_hungry = is_hungry

    def get_is_need_a_vet(self):
        return self.__is_need_a_vet

    def set_is_need_a_vet(self, is_need_a_vet):
        self.__is_need_a_vet = is_need_a_vet
