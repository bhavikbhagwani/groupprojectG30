"""
Dice class
This class has one job which is to roll a dice and return its value
"""

import random

class Dice:
    
    def roll(self):
        dice_value = random.randint(1,6)
        return dice_value