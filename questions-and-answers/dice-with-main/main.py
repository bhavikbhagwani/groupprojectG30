#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for using a class rolling dices."""

import dice


def main():
    """Use and roll the dice."""
    die = dice.Dice()

    roll = die.roll()
    print("Rolling the dice, it was a {}".format(roll))

    roll = die.roll()
    print("Rolling the dice, it was a {}".format(roll))

    number = die.get_rolls_made()
    print("You have rolled the dice {} times.".format(number))


if __name__ == '__main__':
    main()
