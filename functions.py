#!/usr/bin/env python3
def start_message():
    """Displays game's start message"""
    message = '''You will have a number of tasks to comeplete in each city.
    You will have to complete all the tasks in the current city to move on.
    Good Luck, you will need it!'''


def user_name():
    """Returns the name of player"""
    name = input("Enter your name: ")
    return name


def user_age():
    """Returns the player's age"""
    age = int(input("Enter your age: "))
    return age


def age_storage():
    """Stores the ages of all the users who ever played game"""
    age_list = []
    while True:
        age = user_age()
        age_list.append(age)
        break
    print(age_list)


def character_health():
    """Stores the health of character.
    Always starts with 100 health"""
    health = 100
    return health


def busted_pop_up():
    """Prints "BUSTED" when caught by police"""
    message = 'busted'
    print(message.upper())


def no_weapon_warning():
    """Prints warning of game difficulty when user does not have a weapon in inventory"""
    message = "Without a weapon this game will be more difficult. Let's go!"
    print(message)


def dead_pop_up():
    """Prints when character dies"""
    message = 'you died!'
    print(message.upper())


def ending_message():
    """Prints message when game is over"""
    message = "thank you for playing"
    print(message.upper())


def congratulations_message():
    """Congratulates player"""
    message = 'congratulations'
    print(message.upper())


def want_to_play():
    """Asks the user if they want to play game"""
    question = input("\nDo you wish to play? (yes/no) ").lower()
    return question.lower()


def weapon_select():
    """Prompts player to choose one of 3 weapons and adds it to the character's inventory"""
    inventory = []
    weapon = input("\nPlease choose a weapon. "
                   "You only have one chance to choose."
                   "Choose wisely!"
                   "(gun/stick/none) ").lower()
    if weapon == 'gun':
        inventory.append('gun')
        print("\nAll ready, lets go.")
    elif weapon == 'stick':
        inventory.append('stick')
        print("\nAll ready, lets go.")
    elif weapon == 'none':
        print(f"\n{no_weapon_warning()}")


def welcome_message():
    """Welcomes the user to the game"""
    if want_to_play() == 'yes':
        print(f'''Welcome {user_name().title()},
        You are stating with {character_health()} health.
        Good Luck!''')



age_storage()