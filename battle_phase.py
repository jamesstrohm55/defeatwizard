import os 

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


