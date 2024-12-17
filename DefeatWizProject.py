import random
import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Base Character Class
class Character:
    def __init__(self, name, health, attack_power,): 
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        die1 = random.randint(1, 20)
        opponent.health -= die1
        print (f"{self.name} did {die1} damage to {opponent.name}!")
        

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        self.health += 25
        print(f"{self.name} healed for {self.health} points.")

    def special_ability(self):
        pass

    def alt_ability(self):
        pass


#------------------------------------------------------------------------------------------------------------------


#Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=random.randint(1, 20))

    #Drakecleaver ability
    def special_ability(self, opponent):
        drakecleaver = random.randint(1, 20)
        multiplier = random.randint(2, 5)
        de_spec = drakecleaver * multiplier
        opponent.health -= de_spec
        print(f"{self.name} used Drakecleaver and dealt {drakecleaver} damage with a multiplier of x{multiplier} to {opponent.name}!")

    #Hydrablood regenerative ability
    def alt_ability(self, opponent):
        self.health = random.randint(75, 100)
        opponent.health = opponent.health
        print(f"{self.name} used Hydrablood ability to regenerate half health!")
        
    def heal(self):
        return super().heal()

#Mage Class   
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=random.randint(1, 20))

    #Dark Blade attack
    def special_ability(self, opponent):
        dark_blade = random.randint(10, 20)
        multiplier = random.randint(2, 5)
        ken_spec = dark_blade * multiplier
        opponent.health -= ken_spec
        print(f"{self.name} slashed {opponent.name} with their Dark Blade and dealt {dark_blade} damage with a multiplier of x{multiplier}!")

    #Shadow Strike attack
    def alt_ability(self, opponent):
        shadow_stike = random.randint(15, 20)
        multiplier = random.randint(2, 5)
        ken_alt = shadow_stike * multiplier
        opponent.health -= ken_alt
        print(f"{self.name} dissapeared into the Shadow Realm and struck from the dark with Shadow Strike causing {shadow_stike} damage to {opponent.name} with a multiplier of x{multiplier}!")

    def heal(self):
        return super().heal()

#Minotaur Class
class Minotaur(Character):
    def __init__(self, name):
        super().__init__(name, health=300, attack_power=random.randint(1, 20))

    #Greataxe Attack
    def special_ability(self, opponent):
        greataxe = random.randint(15, 20)
        multiplier = random.randint(2, 5)
        min_spec = greataxe * multiplier
        opponent.health -= min_spec
        print(f"{self.name} hit {opponent.name} with their Greataxe for {greataxe} damage with a multiplier of x{multiplier}!")

    #Horn Charge Ability
    def alt_ability(self, opponent):
        horn_charge = random.randint(1, 20)
        multiplier = random.randint(2, 5)
        min_alt = horn_charge * multiplier
        opponent.health -= min_alt
        print(f"{self.name} charged forth with their horns down and hit {opponent.name} for {horn_charge} damage with a muliplier of x{multiplier}!")
        
    def heal(self):
        return super().heal()

# Dwarf Class
class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name, health=500, attack_power=random.randint(1, 20))

    #Gold Greed Ability
    def special_ability(self, opponent):
        hand_o_greed = random.randint(10, 20)
        multiplier = random.randint(2, 5)
        d_spec = hand_o_greed * multiplier
        opponent.health -= d_spec
        print(f"{self.name} noticed the gold around {opponent.name}'s neck and was infuriated to find it in the hands of a race other than a Dwarf's. He becomes angry and attacks {opponent.name} for {hand_o_greed} with a critical multiplier of x{multiplier} to snatch it back!")

    #Oakenshield Ability    
    def alt_ability(self, opponent):
        opponent.attack_power = 1
        print(f"{opponent.name}'s attack falls due to {self.names}'s use of Oakenshield, an inpenetrable shield!")


#--------------------------------------------------------------------------------------------------------------------------------


# Evil Wizard "Galexialyn Strain"
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=500, attack_power=random.randint(1, 25))

    #Regeneration Ability for Wizard
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health is {int(self.health)}")


#------------------------------------------------------------------------------------------------------------------------------


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
    

#------------------------------------------------------------------------------------------------------------------------------------


# Enter battle phase
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print('')
        print("----Player Stats----")
        print(player.display_stats())
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Alternate Special Ability")
        print("4. Heal")

        choice = (input("Choose an action: "))
        os.system("cls")
        
        print("----Game Log----")
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard) 
        elif choice == '3':
            player.alt_ability(wizard)
        elif choice == '4':
            player.heal()
        else:
            print("Invalid choice, try again.")
            continue

        #Wizard Attack Phase
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


#------------------------------------------------------------------------------------------------------------------------


# Main function for game flow
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("Galexialyn Strain")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()