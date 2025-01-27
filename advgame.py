'''Group Members Names: - Shekhar Singh (21BCA2245),
                          Riti Srivastava (21BCA1251) and 
                          Sonal Verma (21BCA1768).'''

import random
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious land. Your goal is to find the legendary treasure.")
    print("Where would you like to go? (1. Forest, 2. Cave, 3. Mountain)")

    choice = input("> ")

    if choice == "1":
        explore_forest()
    elif choice == "2":
        enter_cave()
    elif choice == "3":
        climb_mountain()
    else:
        print("Invalid choice. Try again.")
        start_game()

def explore_forest():
    print("You enter the dense forest. It's filled with ancient trees and hidden creatures.")
    print("What do you want to do? (1. Search for treasure, 2. Follow a path, 3. Return to the starting point)")

    choice = input("> ")

    if choice == "1":
        search_treasure()
    elif choice == "2":
        follow_path()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice. Try again.")
        explore_forest()

def search_treasure():
    print("You search the forest for hidden treasure.")
    print("You find a treasure chest! What do you want to do? (1. Open the chest, 2. Leave it)")

    choice = input("> ")

    if choice == "1":
        open_chest()
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Try again.")
        search_treasure()

def open_chest():
    print("You open the treasure chest and find a rare artifact!")
    print("Congratulations! You have found the legendary treasure.")
    end_game()

def follow_path():
    print("You decide to follow a winding path through the forest.")
    print("The path leads you to a tranquil lake. What do you want to do? (1. Swim in the lake, 2. Continue exploring)")

    choice = input("> ")

    if choice == "1":
        swim_in_lake()
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Try again.")
        follow_path()

def swim_in_lake():
    print("You take a refreshing swim in the lake.")
    print("After the swim, you notice a hidden cave nearby. What do you want to do? (1. Enter the cave, 2. Return to the forest)")

    choice = input("> ")

    if choice == "1":
        enter_hidden_cave()
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Try again.")
        swim_in_lake()

def enter_hidden_cave():
    print("You enter the hidden cave and find yourself in a mysterious chamber.")
    print("What do you want to do? (1. Examine the ancient inscriptions, 2. Leave the cave)")

    choice = input("> ")

    if choice == "1":
        examine_inscriptions()
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Try again.")
        enter_hidden_cave()

def examine_inscriptions():
    print("You closely examine the ancient inscriptions and decipher a clue leading to the treasure!")
    print("Congratulations! You have found the legendary treasure.")
    end_game()

def enter_cave():
    print("You enter a dark cave. It's filled with eerie sounds and mysterious echoes.")
    print("What do you want to do? (1. Explore deeper, 2. Return to the starting point)")

    choice = input("> ")

    if choice == "1":
        explore_deeper()
    elif choice == "2":
        start_game()
    else:
        print("Invalid choice. Try again.")
        enter_cave()

def explore_deeper():
    print("You venture deeper into the cave, facing unknown dangers.")
    print("You come across a fork in the cave. Which path do you choose? (1. Left, 2. Right)")

    choice = input("> ")

    if choice == "1":
        take_left_path()
    elif choice == "2":
        take_right_path()
    else:
        print("Invalid choice. Try again.")
        explore_deeper()

def take_left_path():
    print("You take the left path and encounter a giant spider!")
    print("What do you want to do? (1. Fight, 2. Flee)")

    choice = input("> ")

    if choice == "1":
        fight_spider()
    elif choice == "2":
        start_game()
    else:
        print("Invalid choice. Try again.")
        take_left_path()

def fight_spider():
    print("You engage in a fierce battle with the giant spider and emerge victorious.")
    print("You find a hidden passage that leads to a deeper level of the cave!")
    enter_hidden_chamber()

def enter_hidden_chamber():
    print("You enter a hidden chamber with glowing crystals and ancient artifacts.")
    print("There are three doors in front of you. Which door do you choose? (1. Door 1, 2. Door 2, 3. Door 3)")

    choice = input("> ")

    if choice == "1":
        enter_door_1()
    elif choice == "2":
        enter_door_2()
    elif choice == "3":
        enter_door_3()
    else:
        print("Invalid choice. Try again.")
        enter_hidden_chamber()

def enter_door_1():
    print("You open door 1 and find yourself in a labyrinthine maze!")
    print("Navigate through the maze to find the treasure.")

    print("Congratulations! You have found the legendary treasure in the maze!")
    end_game()

def enter_door_2():
    print("You open door 2 and encounter a group of hostile creatures!")
    print("What do you want to do? (1. Fight, 2. Flee)")

    choice = input("> ")

    if choice == "1":
        fight_creatures()
    elif choice == "2":
        start_game()
    else:
        print("Invalid choice. Try again.")
        enter_door_2()

def fight_creatures():
    print("You engage in a challenging battle with the creatures and defeat them.")
    print("Beyond the creatures, you find a hidden passage that leads to the legendary treasure!")
    end_game()

def enter_door_3():
    print("You open door 3 and step into a room with a magical portal.")
    print("The portal transports you to a different dimension!")
    print("To return, you must solve a series of puzzles in this dimension.")
 
    print("Congratulations! You have solved all the puzzles and returned to the hidden chamber.")
    print("You find the legendary treasure waiting for you!")
    end_game()

def take_right_path():
    print("You take the right path and discover a hidden treasure chest!")
    print("Congratulations! You have found the legendary treasure.")
    end_game()

def climb_mountain():
    print("You begin your ascent up the treacherous mountain. The wind howls and the air thins.")
    print("What do you want to do? (1. Reach the first checkpoint, 2. Continue climbing, 3. Return to the starting point)")

    choice = input("> ")

    if choice == "1":
        reach_first_checkpoint()
    elif choice == "2":
        continue_climbing()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice. Try again.")
        climb_mountain()

def reach_first_checkpoint():
    print("You reach the first checkpoint on the mountain.")
    print("There is a mountain guide waiting here. She offers you valuable advice.")
    print("What do you want to do? (1. Listen to the guide, 2. Ignore the guide and continue climbing)")

    choice = input("> ")

    if choice == "1":
        listen_to_guide()
    elif choice == "2":
        print("You decide to ignore the guide and continue climbing without her advice.")
        continue_climbing()
    else:
        print("Invalid choice. Try again.")
        reach_first_checkpoint()

def listen_to_guide():
    print("You attentively listen to the mountain guide's advice.")
    print("She tells you about the treacherous ice fields ahead and the importance of proper gear.")
    print("What do you want to do? (1. Obtain the necessary gear, 2. Continue climbing without gear)")

    choice = input("> ")

    if choice == "1":
        obtain_gear()
    elif choice == "2":
        continue_climbing_without_gear()
    else:
        print("Invalid choice. Try again.")
        listen_to_guide()

def obtain_gear():
    print("You search for a nearby mountaineering supply store and acquire the necessary gear.")
    print("With the proper gear, you continue your climb up the mountain.")
    continue_climbing()

def continue_climbing_without_gear():
    print("You decide to continue climbing without the necessary gear.")
    print("As you progress, you encounter icy slopes that are difficult to traverse without proper equipment.")
    print("You slip and fall, making it impossible to continue.")
    print("Game Over.")

def continue_climbing():
    print("You continue your climb up the mountain, facing icy slopes and freezing temperatures.")
    print("You reach a point where the path splits. Which path do you choose? (1. Left, 2. Right)")

    choice = input("> ")

    if choice == "1":
        take_left_path()
    elif choice == "2":
        take_right_path()
    else:
        print("Invalid choice. Try again.")
        continue_climbing()

def take_left_path():
    print("You take the left path and encounter a blizzard!")
    print("What do you want to do? (1. Take shelter, 2. Keep pushing forward)")

    choice = input("> ")

    if choice == "1":
        take_shelter()
    elif choice == "2":
        keep_pushing_forward()
    else:
        print("Invalid choice. Try again.")
        take_left_path()

def take_shelter():
    print("You find a small cave and take shelter from the blizzard.")
    print("After waiting for the storm to pass, you continue your climb.")
    continue_climbing()

def keep_pushing_forward():
    print("You brave the blizzard and keep pushing forward, fighting against the harsh conditions.")
    print("Your determination pays off, and you reach a hidden mountain monastery.")
    explore_monastery()

def explore_monastery():
    print("You explore the mountain monastery and encounter wise monks.")
    print("They offer you a challenge to test your inner strength and focus.")
    print("What do you want to do? (1. Accept the challenge, 2. Decline the challenge and continue climbing)")

    choice = input("> ")

    if choice == "1":
        accept_challenge()
    elif choice == "2":
        continue_climbing()
    else:
        print("Invalid choice. Try again.")
        explore_monastery()

def accept_challenge():
    print("You accept the challenge and undergo rigorous mental and physical tests.")
    print("With perseverance, you successfully complete the challenge and gain the monks' blessings.")
    print("They provide you with a special artifact that aids your journey.")
    continue_climbing()

def take_right_path():
    print("You take the right path and face a narrow and treacherous ridge.")
    print("What do you want to do? (1. Cross the ridge carefully, 2. Turn back and take another path)")

    choice = input("> ")

    if choice == "1":
        cross_ridge()
    elif choice == "2":
        continue_climbing()
    else:
        print("Invalid choice. Try again.")
        take_right_path()

def cross_ridge():
    print("You carefully navigate the narrow ridge, facing strong winds and vertigo-inducing heights.")
    print("With steady nerves and careful steps, you successfully cross the ridge.")
    print("Congratulations! You have reached the summit of the mountain.")
    print("You find the legendary treasure waiting for you!")
    end_game()

def end_game():
    print("Congratulations! You have completed the adventure.")
    print("Thank you for playing!")
    exit()
start_game()
