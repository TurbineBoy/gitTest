#!/usr/bin/env python3

"""
Creating a vending machine with 4 rows and 4 columns that is placed within a school.
This vending machine accepts bills (10, 5 & 2) but only takes dollar coins and 25 cent pieces.
"""
import time
import random
import datetime


def welcome_message():
    """Constantly displays welcome message before money is placed in the machine."""
    print("Hello, what are you having today?")
    print("""Please note this machine only takes:
    Bills: 10, 5, 2
    Coins: 1.00, 0.25""")


def display_keypad():
    """Displays the keys for the vending machine."""
    print("Please make a selection")
    keys = [['A1', 'A2', 'A3', 'A4'],
            ['B1', 'B2', 'B3', 'B4'],
            ['C1', 'C2', 'C3', 'C4'],
            ['D1', 'D2', 'D3', 'D4'],
            ['**', 'YES', 'NO']]
    for key in keys:
        for i in key:
            print(f'\t{i}', end='')
        print()
    return keys


def storing_what_is_in_machine():
    """Stores information of what is in machine at any given time."""
    bottled_drinks = ['water', 'sprite', 'cran-water', 'iced coffee']
    juices = ['mango juice', 'cherry juice', 'black-currant juice', 'orange juice']
    snacks = ['fruit snacks', 'nuts', 'granola bar', 'snickers']
    stationery = ['pencil', 'eraser', 'book', 'paper pack']

    # categories_of_items = [bottled_drinks, juices, snacks, stationery]

    items = {'bottled drinks': bottled_drinks,
             'juices': juices,
             'snacks': snacks,
             'stationery': stationery}
    return items


def display_machine_options():
    """Displays the goods available for purchase from the machine."""
    bottled_drinks = ['water', 'sprite', 'cran-water', 'iced coffee']
    juices = ['mango juice', 'cherry juice', 'black-currant juice', 'orange juice']
    snacks = ['fruit snacks', 'nuts', 'granola bar', 'snickers']
    stationery = ['pencil', 'eraser', 'book', 'paper pack']

    items = {'bottled drinks': bottled_drinks,
             'juices': juices,
             'snacks': snacks,
             'stationery': stationery}
    for values in items.values():
        for i in values:
            print(f' | {i}', end="")
        print()


def prices_of_items():
    """Stores the prices of items."""
    bottled_drinks = ['water', 'sprite', 'cran-water', 'iced coffee']
    juices = ['mango juice', 'cherry juice', 'black-currant juice', 'orange juice']
    snacks = ['fruit snacks', 'nuts', 'granola bar', 'snickers']
    stationery = ['pencil', 'eraser', 'book', 'paper pack']

    item_price = {'2.50': bottled_drinks,
                  '2.00': juices,
                  '3.00': snacks,
                  '3.75': stationery}
    for price, items in item_price.items():
        for item in items:
            print(f"{item}: {price}")
        print()


def assigning_buttons_to_items():
    """Assigns the buttons of machine to the items in machine."""
    bottled_drinks = ['water', 'sprite', 'cran-water', 'iced coffee']
    juices = ['mango juice', 'cherry juice', 'black-currant juice', 'orange juice']
    snacks = ['fruit snacks', 'nuts', 'granola bar', 'snickers']
    stationery = ['pencil', 'eraser', 'book', 'paper pack']

    programmed_buttons = {'A1': bottled_drinks[0], 'A2': bottled_drinks[1],
                          'A3': bottled_drinks[2], 'A4': bottled_drinks[3],

                          'B1': juices[0], 'B2': juices[1], 'B3': juices[2], 'B4': juices[3],

                          'C1': snacks[0], 'C2': snacks[1], 'C3': snacks[2], 'C4': snacks[3],

                          'D1': stationery[0], 'D2': stationery[1], 'D3': stationery[2], 'D4': stationery[3],

                          '**': 'Give back money.',

                          'YES': 'YES', 'NO': 'NO'}
    return programmed_buttons


"""
def money_detection():
    # User places money in the machine
    bills = {'10.00': 0, '5.00': 0, '2.00': 0}
    coins = {'1.00': 0, '0.25': 0}
    initial_money = 0
"""


def user_making_choice():
    """User making a selection."""
    bottled_drinks = ['water', 'sprite', 'cran-water', 'iced coffee']
    juices = ['mango juice', 'cherry juice', 'black-currant juice', 'orange juice']
    snacks = ['fruit snacks', 'nuts', 'granola bar', 'snickers']
    stationery = ['pencil', 'eraser', 'book', 'paper pack']

    programmed_buttons = {'A1': bottled_drinks[0], 'A2': bottled_drinks[1],
                          'A3': bottled_drinks[2], 'A4': bottled_drinks[3],

                          'B1': juices[0], 'B2': juices[1], 'B3': juices[2], 'B4': juices[3],

                          'C1': snacks[0], 'C2': snacks[1], 'C3': snacks[2], 'C4': snacks[3],

                          'D1': stationery[0], 'D2': stationery[1], 'D3': stationery[2], 'D4': stationery[3],

                          '**': 'Give back money.',

                          'YES': 'YES', 'NO': 'NO'}

    key = input("Choose an item: ").lower()
    machine_active = True
    while machine_active:
        # For bottled drinks
        if key == 'A1':
            print(f"You chose {programmed_buttons['A1']}.")
            return
        elif key == 'A2':
            print(f"You chose {programmed_buttons['A2']}")
            return
        elif key == 'A3':
            print(f"You chose {programmed_buttons['A3']}.")
            return
        elif key == 'A4':
            print(f"You chose {programmed_buttons['A4']}.")
            return

        # For juices
        elif key == 'B1':
            print(f"You chose {programmed_buttons['B1']}.")
            return
        elif key == 'B2':
            print(f"You chose {programmed_buttons['B2']}")
            return
        elif key == 'B3':
            print(f"You chose {programmed_buttons['B3']}.")
            return
        elif key == 'B4':
            print(f"You chose {programmed_buttons['B4']}.")
            return

        # For snacks
        elif key == 'C1':
            print(f"You chose {programmed_buttons['C1']}.")
            return
        elif key == 'C2':
            print(f"You chose {programmed_buttons['C2']}")
            return
        elif key == 'C3':
            print(f"You chose {programmed_buttons['C3']}.")
            return
        elif key == 'C4':
            print(f"You chose {programmed_buttons['C4']}.")
            return

        # For stationery
        elif key == 'D1':
            print(f"You chose {programmed_buttons['D1']}.")
            return
        elif key == 'D2':
            print(f"You chose {programmed_buttons['D2']}")
            return
        elif key == 'D3':
            print(f"You chose {programmed_buttons['D3']}.")
            return
        elif key == 'D4':
            print(f"You chose {programmed_buttons['D4']}.")
            return

        # For special keys
        elif key == '**':
            print("Retrieving money.")
            return
        # 'YES' and 'NO' dealt with in a separate function
    ending_message()
    return key


def vending_machine_inuse():
    """After user has made choice, vending machine releases the item."""
    active = True
    while active:
        display_machine_options()
        print()
        display_keypad()
        user_making_choice()
        active = False


def ending_message():
    """Printed ending message when transaction is complete."""
    time_of_day = datetime.datetime.now()
    if 0 <= time_of_day.hour <= 11:
        print(f"Thank you! Enjoy your morning.")

    elif 12 <= time_of_day.hour <= 16:
        print(f"Thank you! Enjoy your afternoon.")
    else:
        print(f"Thank you! Enjoy your night.")


def main():
    """Main function"""
    welcome_message()
    print()
    time.sleep(1)
    display_keypad()
    display_machine_options()
    user_making_choice()
    ending_message()

