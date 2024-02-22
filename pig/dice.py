import random

class Dice:
    
    def roll(self):
        dice_value = random.randint(1,6)
        return dice_value