# Import the necessary packages
from cat import Cat, print_all_cats
from dog import Dog, print_all_dogs
from temporary_home import Temporary_home
from foundation import Foundation


def enter_dog_data():
    name = input("Whats the name of animal? ")
    age = input("How old is he/she? (years) ")
    weight = input("how much does this animal weight(kg)? ")
    gender = input("What the gender she/he have?(male/female) ")
    dog_breed = input("Whats the breed of animal? ")
    is_hungry = input("Is hungry? yes/no ")
    is_need_a_vet = input("Is need a vet? yes/no ")
    dog = Dog(name, age, weight, gender, dog_breed, is_hungry, is_need_a_vet)
    print("\nNew dog added:", "\nDog name:", dog.get_name(), "\nDog age:", dog.get_age(),
          "\nDog gender:", dog.get_gender(), "\nDog weight:", dog.get_weight(),
          "\nDog breed:", dog.get_dog_breed(), '\nIs hungry:?', dog.get_is_hungry(),
          '\nIs need a vet? ', dog.get_is_need_a_vet(), sep=' ')

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
    print("\nNew Cat added:", "\nCat name:", cat.get_name(), "\nCat age:", cat.get_age(),
          "\nCat gender:", cat.get_gender(), "\nCat weight:", cat.get_weight(),
          "\nCat breed:", cat.get_dog_breed(), '\nIs hungry:?', cat.get_is_hungry(),
          '\nIs need a vet? ', cat.get_is_need_a_vet(), sep=' ')


ans = True
while ans:
    print("""
    This is a program for managing the foundation dealing with homeless animals...
    
    1.Check list of ours animals
    2.Add new dog
    3.Add new cat
    3.Check actual info about our foundation
    4.Make the necessary purchases for animals
    5.Add a new temporary home for animals
    6.Check is some animal needs eat
    7.Check is some animal need go to vet
    8.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        print_all_dogs()
        print_all_cats()
    elif ans == "2":
        enter_dog_data()
        print("New dog added")
    elif ans == "3":
        enter_cat_data()
        print("New_cat added")
    elif ans == "4":
        print("\n Goodbye")
        ans = None
    else:
        print("\n Not Valid Choice Try again")
