class Animal(object):
    def __init__(self, name, age, weight, gender):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__gender = gender

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self._age = age

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self._weight = weight

    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self._weight = gender
