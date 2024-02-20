#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class rolling dices."""

import random


class Dice():
    """Example of dice class."""

    faces = 6
    last_roll = None

    def __init__(self):
        """Roll a dice once and return the value."""
        random.seed()
        self.rolls_made = 0

    def roll(self):
        """Roll a dice once and return the value."""
        self.rolls_made += 1
        self.last_roll = random.randint(1, self.faces)
        return self.last_roll

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made

    def print_last_roll(self):
        """Print out the last roll made."""
        output = (
            "Last roll made was {} which "
            "was the {} roll in the serie."
        )
        print(output.format(self.last_roll, self.rolls_made))
