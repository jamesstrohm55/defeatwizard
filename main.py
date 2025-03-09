import random
import os
from battle_phase import battle
from create_characters import create_character
from players import EvilWizard
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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