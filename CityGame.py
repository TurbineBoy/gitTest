#!/usr/bin/env python3
"""
We are creating a game called ________
It is about a man in a city.

He will have a number of tasks to complete in order to complete the game.

Good Luck!
"""

name = input("What is your name? ")
age = int(input("How old are you? "))  # collecting age data simply to gauge age of players

# variables needed
health = 100
busted_pop_up = "busted"
no_weapon_choice = "without a weapon this game will be more difficult. Let's go!"
dead_pop_up = "you died!"
end_game_message = "thank you for playing!"
_5min_message = "5 minutes later"
congrats_message = "congratulations"

# list of what is in your inventory.
inventory = []

# locations on map to choose from
map = ['linx city', ]

want_to_play = input("\nDo you wish to play? (yes/no) ").lower()
if want_to_play == 'yes':
    print(f"\nWelcome {name.title()}, hope you enjoy!")
    print(f"You are starting with {health} health.")
    print("Let's go!")

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
        print(f"\n{no_weapon_choice.upper()}")

    # outputting list of inventry at start
    print(f"\nYou currently have the following items in your inventory: {inventory}")

    print("\nYou begin on a long dirt road with sirens all around you and city lights in the near distance.")
    hide_or_run = input("Do you hide until the sirens stop or do you run to the near by lights? (hide/run) ").lower()
    if hide_or_run == 'hide':
        pop_up = "\nYou hide until the sirens stop"
        print(pop_up.upper())
        print(_5min_message.upper())
        # sirens stop
        print("\nYou come out of hiding and finally run to the city lights in the distance.")

        print("\nWhen you reach the city lights, you come across a motel. \nThe owner tells you that you look"
              " tired and in need of rest.")
        sleep_or_leave = input("Do you sleep at the motel or stay on the run? (sleep/run) ").lower()
        if sleep_or_leave == 'sleep':
            print("\nYou were smart to sleep at the motel and gained 100 health.")
            health += 100
            print(f"You now have {health} health.")
            print("You need to get a move on.")
            print("You leave the motel and head deeper into the city.")
            # game skips over when in the city.
        elif sleep_or_leave == 'run':
            print("\nIt would've been wise to sleep at the motel.")
            print("Not sleeping costs you 5 health.")
            health -= 5
            print(f"You now have {health} health.")

        '''
        Both of these option allowing to continue the game.
        The screen fades and reappears with you on the side of the road deep in the city.
        You do not know where you are.
        What will you do next?
        '''

        print("\nYou walk around the city trying to avoid police.")
        print("You ask a random person where you are.")

        '''
        The game has the option to either tell you where you are or to slap you...
        If they slap you, it gets interesting.
        Lets play!!

        For now, you manually choose what the game does.
        '''

        print("\n'Excuse me, may you please tell me where I am?'")
        tell_or_slap = input("Does this person tell you or slap you? (tell/slap) ").lower()
        if tell_or_slap == 'tell':
            print("\n'You are in Linx City, do you need help finding your way?'")

            yes_or_no = input("Do you need help? (yes/no) ").lower()
            if yes_or_no == 'yes':
                print("\nHere's a map, I have to go now. I hope this helps you.")
                inventory.append('map')
                print(f"\nYou currently have the following items in your inventory: {inventory}")
                print("\nYou look at the map and see a few possible places you can go.")
                print(f"Options: {map}")
                print(f"---Other locations are locked until you finish in {map[0]}.")

                '''
                You now have the option to travel to one of two cities.
                In these cities, you will have 2 tasks each.
                Complete these two tasks to complete the game.

                When you select a city, the screen will fade and you will appear in the city you chose.
                '''

                map_travel = input("Where would you like to go? ").lower()
                for city in map:
                    for go in map_travel:
                        if city == map[0]:
                            print(f"\nGoing to {map[0].title()}!")
                            print("You have two tasks to complete,\n"
                                  "Tasks: \n"
                                  "1. Locate the 'Linx' and feed it.\n"
                                  "2. Capture the 'Linx' while it's eating. ")

                            print(f"\nAs you appear in {map[0].title()}, "
                                  f"the 'Linx' attacks you and you lose 20 health.")
                            health -= 20
                            print(f"You now have {health} health.")
                            print("You can either choose to fight the 'Linx' or feed him.")
                            fight_or_feed = input("Do you fight or feed the 'Linx'? (fight/feed) ").lower()
                            if fight_or_feed == 'fight':
                                print("\nThe 'Linx' kills you with one bite.")
                                health -= health
                                print(f"Health: {health}")
                                print(dead_pop_up.upper())
                                print(end_game_message.upper())
                                break

                            elif fight_or_feed == 'feed':
                                print("\nYou approach the 'Linx' as it stares at you curiously.")
                                print("You toss a couple berries at it hoping it eats them.")

                                '''
                                Manually put in if 'Linx' eats berries or not.
                                '''

                            eat_or_not = input("Does the 'Linx' eat the berries? (yes/no) ").lower()
                            if eat_or_not == 'yes':
                                print("\nThe 'Linx' successfully eats the berries.")
                                print("You should try to capture the 'Linx'.")
                                print("Will you successfully capture it?")

                                '''
                                Manually input if capture is successful.
                                '''
                                successful_or_bust = input("Is the capture successful? (success/unsuccessful) ").lower()
                                if successful_or_bust == 'success':
                                    print("\nYou have successfully caught the 'Linx'.")
                                    print("You have completed the game.")
                                    print(congrats_message.upper())
                                    break
                                    # keep break until ready to input code for other cities
                                else:
                                    print("\nYou failed at catching the 'Linx'.")
                                    print("It kills you immediately.")
                                    health -= health
                                    print(f"Health: {health}")
                                    print(dead_pop_up.upper())
                                    print(end_game_message.upper())
                                    break

                            else:
                                print("\nThe 'Linx' is not intrigued by the berries "
                                      "and brutally attacks and kills you instantly.")
                                health -= health
                                print(f"Health: {health}")
                                print(dead_pop_up.upper())
                                print(end_game_message.upper())
                                break

                                # You have finished in Linx City, the other cities on the map have unlocked.


            else:
                print("No, I will find my way thank you!!")
                # complete code to find your way

        elif tell_or_slap == 'slap':
            print("The person slaps you and you have the option to retaliate or to walk away.")
            # finish code for when person slaps you

    elif hide_or_run == 'run':
        print("\nYou die in a shoot out with police.")
        inventory.pop(0)
        health -= health
        print(dead_pop_up.upper())
        print(end_game_message.upper())

else:
    print("Goodbye!")
