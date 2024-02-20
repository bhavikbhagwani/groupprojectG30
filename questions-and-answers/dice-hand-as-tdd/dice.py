#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class rolling dices."""

import random


class Dice:
    """Example of dice class."""

    # class variable shared by all instances
    faces = 6

    def __init__(self):
        """Roll a dice once and return the value."""
        random.seed()
        # instance variable unique to each instance
        self.rolls_made = 0
        self.sum_all_rolls = 0
        self.last_roll = None

    def set_faces(self, faces):
        """Set the faces on the dice."""
        self.faces = faces
        print(f"The faces of the die are now: {self.faces}")

    def roll(self):
        """Roll a dice once and return the value."""
        self.rolls_made += 1
        self.last_roll = random.randint(1, self.faces)
        self.sum_all_rolls += self.last_roll
        return self.last_roll

    def get_last_roll(self):
        """Return last roll."""
        return self.last_roll

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made

    def get_sum_rolls(self):
        """Get sum of all rolls made."""
        return self.sum_all_rolls
