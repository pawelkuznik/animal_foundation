# Import the necessary packages
from cat import Cat, print_all_cats, print_cat_info, if_anyone_cat_is_hungry, if_anyone_cat_need_go_to_vet
from dog import Dog, print_all_dogs,print_dog_info, if_anyone_dog_is_hungry, if_anyone_dog_need_go_to_vet
from temporary_home import TemporaryHome, print_temp_home
from foundation import Foundation, check_foundation_info

# create object of our foundaton (it should getting data from file/database)
our_foundation = Foundation('wroclaw', 'Pawel Kuznik', 30000, 'NewHope')


def enter_dog_data():
    name = input("Whats the name of animal? ")
    age = input("How old is he/she? (years) ")
    weight = input("how much does this animal weight(kg)? ")
    gender = input("What the gender she/he have?(male/female) ")
    dog_breed = input("Whats the breed of animal? ")
    is_hungry = input("Is hungry? yes/no ")
    is_need_a_vet = input("Is need a vet? yes/no ")
    dog = Dog(name, age, weight, gender, dog_breed, is_hungry, is_need_a_vet)
    print_dog_info(dog)

#TODO: It should be parametrize (enter_animal_data() to not duplicate code


def enter_cat_data():
    name = input("Whats the name of animal? ")
    age = input("How old is he/she? (years) ")
    weight = input("how much does this animal weight(kg)? ")
    gender = input("What the gender she/he have?(male/female) ")
    dog_breed = input("Whats the breed of animal? ")
    is_hungry = input("Is hungry? yes/no ")
    is_need_a_vet = input("Is need a vet? yes/no ")
    cat = Cat(name, age, weight, gender, dog_breed, is_hungry, is_need_a_vet)
    print_cat_info(cat)


def enter_temp_home_data():
    name = input('Temporary home  name is: ')
    address = input('Address is: ')
    actual_free_space_to_animal = input('Actual free space to animals: ')
    temp_home = TemporaryHome(name, address, actual_free_space_to_animal)
    print_temp_home(temp_home)


ans = True
while ans:
    print("""
    This is a program for managing the foundation dealing with homeless animals...
    
    1.Check list of ours animals
    2.Add new dog
    3.Add new cat
    4.Check actual info about our foundation
    5.Make the necessary purchases for animals
    6.Add a new temporary home for animals (home where animals wait to adoption)
    7.Check is some animal needs eat
    8.Check is some animal need go to vet
    9.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        print_all_dogs()
        print_all_cats()
    elif ans == "2":
        enter_dog_data()
        print("New dog added")
        input()
    elif ans == "3":
        enter_cat_data()
        print("New_cat added")
        input()
    elif ans == "4":
        check_foundation_info(our_foundation)
    elif ans == "5":
        print('tst')
    elif ans == "6":
        enter_temp_home_data()
    elif ans == "7":
        if_anyone_dog_is_hungry()
        if_anyone_cat_is_hungry()
    elif ans == "8":
        if_anyone_dog_need_go_to_vet()
        if_anyone_cat_need_go_to_vet()
    elif ans == "9":
        print("\n Goodbye have a nice day!")
        ans = None
    else:
        print("\n Not Valid Choice Try again")
