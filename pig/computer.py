"""
Computer class.

This class instantiates the Computer.
and contains some methods to set difficulty of the computer
and return a dice value according to the computer's difficulty
"""

import random
import dice

class Computer:
    """computer class"""
    def __init__(self):
        """init method"""
        self.name = "computer"
        self.score = 0
        self.current_round_score = 0
        self.difficulty = None
        self.dice = dice.Dice()
        self.num_rounds = 0
    
    def set_computer_difficulty(self, difficulty):
        """setter method to set difficulty"""
        self.difficulty = difficulty
    
    def return_computer_rolled_dice_value(self):
        """method to return dice_value by difficulty"""
        if self.difficulty == "easy":
            easy_list_of_dice_values = [1, 1, 2, 2, 3, 4, 5, 6]
            return random.choice(easy_list_of_dice_values)
        elif self.difficulty == "medium":
            return self.dice.roll()
        else:
            hard_list_of_dice_values = [1, 2, 3, 4, 4, 5, 5, 6, 6]
            return random.choice(hard_list_of_dice_values)
        