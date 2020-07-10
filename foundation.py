from institution import Institution


def check_foundation_info(foundation):
    print("\nOur foundation ", foundation.get_name(), '\nOn adress: ', foundation.get_address()

          , "\nOur owner is: ", foundation.get_owner(), '\nOur money left:', foundation.get_budget())


class Foundation(Institution):
    def __init__(self, address, owner, budget, name):
        super().__init__(address, owner)
        self.__budget = budget
        self.__name = name

    def set_budget(self, budget):
        self.__budget = budget

    def get_budget(self):
        return self.__budget

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


