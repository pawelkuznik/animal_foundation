class Institution:
    def __init__(self, address, owner):
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner


