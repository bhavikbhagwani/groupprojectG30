#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for using a class rolling dices.

This file contains the main program which is the start entry for the program.

It starts by importing the classes and modules needed.

Then it defines the main function that carries out the hole application.

At the bottom is a general constructs which calls the main  function when this
particular file is called using the python interpretator:

    $ python main.py
    Rolling the dice, it was a 6
    Rolling the dice, it was a 4
    You have rolled the dice 2 times.

You can also start the program with an argument to roll the dice more times.

    $ python main.py 7

"""

import sys
import dice


def main():
    """
    Use and roll the dice.

    Start by instantiating an object from the Dice class.
    This will also call the class constructor which is named __init__() in
    the class.
    """
    die = dice.Dice()

    # Use the object and roll the dice and print out its value.
    roll = die.roll()
    print(f"Rolling the dice, it was a {roll}")

    # Use the object and roll the dice again and print out its value.
    roll = die.roll()
    print(f"Rolling the dice, it was a {roll}")

    # Use the argv to roll several times, if its set.
    if len(sys.argv) == 2:
        num_rolls = sys.argv[1]
        print(f"Doing many ({num_rolls}) rolls:")
        for _ in range(int(num_rolls)):
            roll = die.roll()
            print(f" Rolling the dice, it was a {roll}")

    # Check how many rolls has been made, by calling a method of the dice
    # object.
    number = die.get_rolls_made()
    print(f"You have rolled the dice {number} times.")

    # Check how many rolls has been made, by calling a method of the dice
    # object.
    dice_sum = die.get_sum_rolls()
    print(f"The sum of all rolls where {dice_sum}")

    # Change the faces of the dice and roll it again.
    die.set_faces(32)
    roll = die.roll()
    print(f"Rolling the dice, it was a {roll} using faces={die.faces}")


if __name__ == "__main__":
    # Call the main function.
    main()
