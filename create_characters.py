import os
from players import Warrior, Mage, Minotaur, Dwarf


#Player Creation Menu
def create_character():
    os.system("cls")
    print("---Choose your Character!---")
    print("1. Warrior")
    print("2. Mage")
    print("3. Minotaur")
    print("4. Dwarf")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")
    os.system("cls")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Minotaur(name)
    elif class_choice == '4':
        return Dwarf(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    

