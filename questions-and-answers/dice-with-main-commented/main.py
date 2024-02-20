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
"""

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
    print("Rolling the dice, it was a {}".format(roll))

    # Use the object and roll the dice again and print out its value.
    roll = die.roll()
    print("Rolling the dice, it was a {}".format(roll))

    # Check how many rolls has been made, by calling a method of the dice
    # object.
    number = die.get_rolls_made()
    print("You have rolled the dice {} times.".format(number))


if __name__ == '__main__':
    # Call the main function.
    main()
