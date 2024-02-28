"""
Dice class.

This class has one job which is to roll a dice and return its value.
"""


import random


class Dice:
    """Example of Dice class."""

    def __init__(self):
        """Init Dice."""
        self.faces = 6

    def roll(self):
        """Roll a dice once and return the value."""
        dice_value = random.randint(1, self.faces)
        return dice_value
