#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a graphical dices inheriting from a dice.

The class Dice_graphic extends and specialises the Dice by
adding a graphical representation to a 6 faced dice.
"""

import dice


class Dice_graphic(dice.Dice):
    """Example of graphical dice class."""

    # class variable shared by all instances
    # visual = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    visual = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]"]

    def __init__(self):
        """Init the object."""
        super(Dice_graphic, self).__init__()
        print("dice graphic init")

    def graphic(self):
        """Get the representation of the dice."""
        return self.visual[self.last_roll - 1]
