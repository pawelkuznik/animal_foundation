# Import the necessary packages
from cat import Cat
from dog import Dog
from temporary_home import Temporary_home
from foundation import Foundation

ans=True
while ans:
    print("""
    This is a program for managing the foundation dealing with homeless animals...
    
    1.Check list of ours animals
    2.Add new cat
    3.Add new dog
    3.Check actual info about our foundation
    4.Make the necessary purchases for animals
    5.Add a new temporary home for animals
    5.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      new = Dog('spaniel', 12, 24, 'male', 'spaniel')
      print("New dog added")
    elif ans=="2":
      print("\n Student Deleted")
    elif ans=="3":
      print("\n Student Record Found")
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")