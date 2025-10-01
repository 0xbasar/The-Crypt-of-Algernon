import time
import random

def print_slow(text):
    """Prints text slowly to create a more immersive experience."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_player_name():
    """Gets the player's name."""
    return input("What is your name, brave adventurer? ")

def display_intro():
    """Displays the game's introduction."""
    print_slow("\nWelcome to the Crypt of Algernon, a place of mystery and danger.")
    print_slow("You are a renowned adventurer, seeking the fabled Sunstone.")
    print_slow("Legend says it is hidden deep within this crypt, guarded by ancient magic and a fearsome beast.")
    print_slow("Your quest begins now. Good luck.\n")
    input("Press Enter to continue...")

def make_choice(choices):
    """Prompts the player to make a choice from a list of options."""
    while True:
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        player_input = input("> ")
        if player_input.isdigit():
            index = int(player_input) - 1
            if 0 <= index < len(choices):
                return choices[index]
        print_slow("Invalid choice. Please try again.")

def entrance_hall():
    """The first room of the crypt."""
    print_slow("\nYou find yourself in a grand entrance hall.")
    print_slow("The air is thick with the smell of dust and decay.")
    print_slow("Torches flicker on the walls, casting long, dancing shadows.")
    print_slow("Before you are three doors: one to the left, one in the center, and one to the right.")
    
    choice = make_choice(["Go through the left door.", "Go through the center door.", "Go through the right door."])
    
    if choice == "Go through the left door.":
        puzzle_room()
    elif choice == "Go through the center door.":
        monster_lair()
    else:
        treasure_chamber()

def puzzle_room():
    """A room with a riddle puzzle."""
    global has_key
    if has_key:
        print_slow("\nYou are back in the puzzle room. The pedestal is empty.")
        entrance_hall()
        return

    print_slow("\nYou enter a circular room with a stone pedestal in the center.")
    print_slow("On the pedestal is a golden key, shimmering in the torchlight.")
    print_slow("As you approach, a disembodied voice echoes through the room:")
    print_slow("'I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?'")
    
    answer = input("Your answer: ").lower()
    
    if "map" in answer:
        print_slow("\nThe voice says, 'You are wise.' The key is yours.")
        has_key = True
        inventory.append("Golden Key")
    else:
        print_slow("\nThe voice booms, 'You are not worthy!' The floor gives way beneath you!")
        game_over("You fell into a pit of spikes. Your adventure ends here.")

    entrance_hall()

def monster_lair():
    """The lair of the fearsome beast."""
    print_slow("\nYou cautiously open the center door and step into a vast cavern.")
    print_slow("The air is hot and smells of sulfur.")
    print_slow("In the center of the cavern, a giant griffin is sleeping on a pile of bones.")
    
    if "Enchanted Sword" in inventory:
        print_slow("You draw the Enchanted Sword. Its blade glows with a faint blue light.")
        choice = make_choice(["Fight the griffin.", "Sneak past the griffin."])
        
        if choice == "Fight the griffin.":
            fight_griffin()
        else:
            print_slow("You attempt to sneak past the griffin...")
            if random.random() < 0.5:
                print_slow("You successfully sneak past the beast!")
                win_game()
            else:
                print_slow("You step on a loose bone, and the griffin awakens with a roar!")
                game_over("The griffin was too powerful. You have been defeated.")
    else:
        print_slow("You are unarmed! You should find a weapon before facing this beast.")
        entrance_hall()

def treasure_chamber():
    """A room containing treasure (and a trap)."""
    global has_sword
    if has_sword:
        print_slow("\nYou are back in the treasure chamber. The chest is open and empty.")
        entrance_hall()
        return

    print_slow("\nYou enter a small, lavishly decorated chamber.")
    print_slow("In the center of the room is a large, ornate chest.")
    
    if "Golden Key" in inventory:
        print_slow("You use the Golden Key to unlock the chest.")
        print_slow("Inside, you find a magnificent sword, its hilt embedded with jewels.")
        print_slow("You have found the Enchanted Sword!")
        inventory.append("Enchanted Sword")
        has_sword = True
    else:
        print_slow("The chest is locked. You need a key to open it.")
    
    entrance_hall()

def fight_griffin():
    """The final battle with the griffin."""
    print_slow("\nThe griffin lunges at you, its talons extended!")
    player_health = 100
    griffin_health = 150
    
    while player_health > 0 and griffin_health > 0:
        print_slow(f"\nYour health: {player_health}")
        print_slow(f"Griffin's health: {griffin_health}")
        
        choice = make_choice(["Attack with your sword.", "Dodge and try to counter."])
        
        if choice == "Attack with your sword.":
            player_damage = random.randint(20, 35)
            print_slow(f"You strike the griffin for {player_damage} damage!")
            griffin_health -= player_damage
        else:
            if random.random() < 0.6:
                player_damage = random.randint(30, 50)
                print_slow(f"You successfully dodge and counter for {player_damage} damage!")
                griffin_health -= player_damage
            else:
                print_slow("You fail to dodge and the griffin strikes you!")
                player_health -= random.randint(15, 25)

        if griffin_health > 0:
            griffin_damage = random.randint(10, 20)
            print_slow(f"The griffin claws you for {griffin_damage} damage!")
            player_health -= griffin_damage
            
    if player_health > 0:
        print_slow("\nWith a final, mighty blow, you defeat the griffin!")
        win_game()
    else:
        game_over("You fought bravely, but the griffin was too strong.")

def game_over(message):
    """Ends the game with a loss."""
    print_slow(f"\n{message}")
    print_slow("Game Over.")
    play_again()

def win_game():
    """Ends the game with a win."""
    print_slow("\nBeyond the griffin's lair, you find a hidden chamber.")
    print_slow("In the center, resting on a pedestal, is the Sunstone!")
    print_slow("It glows with a warm, brilliant light.")
    print_slow(f"\nCongratulations, {player_name}! You have completed your quest!")
    play_again()

def play_again():
    """Asks the player if they want to play again."""
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        main()
    else:
        print_slow("Thank you for playing!")

def main():
    """The main function to run the game."""
    global player_name, inventory, has_key, has_sword
    
    # Game state variables
    inventory = []
    has_key = False
    has_sword = False
    
    player_name = get_player_name()
    display_intro()
    entrance_hall()

if __name__ == "__main__":
    main()
