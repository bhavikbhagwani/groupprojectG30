#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for using a class rolling dices."""

import sys
import dice


def main():
    """Use and roll the dice."""
    die = dice.Dice()

    roll = die.roll()
    print(f"Rolling the dice, it was a {roll}")

    number = die.get_rolls_made()
    print(f"You have rolled the dice {number} times.")

    dice_sum = die.get_sum_rolls()
    print(f"The sum of all rolls where {dice_sum}")


if __name__ == "__main__":
    main()
