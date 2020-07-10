from institution import Institution


def print_temp_home(temp_home):
    print("\nOur temporary home  name is:  ", temp_home.get_name(), '\nOn adress: ', temp_home.get_address()

          , "\nWe still have free space for animal/s: ", temp_home.get_free_space_animal())




class TemporaryHome(Institution):
    def __init__(self, address, owner, free_space_animal):
        super().__init__(address, owner)
        self.__free_space_animal = free_space_animal

    def get_free_space_animal(self):
        return self.__free_space_animal

    def set_free_space_animal(self, free_space_animal):
        self.__free_space_animal = free_space_animal

