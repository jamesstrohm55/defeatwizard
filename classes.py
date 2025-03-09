import random

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