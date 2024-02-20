#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class rolling dices."""

import random
import dice


class DiceHand:
    """Example of dicehand class."""

    def __init__(self):
        """Init the class."""
        self.hand = []

    def addDices(self, num_dices):
        """Create the dices."""
        for _ in range(num_dices):
            self.hand.append(dice.Dice())

    def roll(self):
        """Roll the dices."""
        for die in self.hand:
            die.roll()

        return self.hand
