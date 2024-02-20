#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class rolling dices."""

import random


class Dice():
    """Example of dice class."""

    faces = 6

    def __init__(self):
        """Roll a dice once and return the value."""
        random.seed()
        self.rolls_made = 0

    def roll(self):
        """Roll a dice once and return the value."""
        self.rolls_made += 1
        return random.randint(1, self.faces)

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made
