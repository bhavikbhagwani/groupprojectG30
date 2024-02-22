import random, dice

class Computer:
    def __init__(self):
        self.name = "computer"
        self.score = 0
        self.current_round_score = 0
        self.difficulty = None
    
    def set_computer_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def return_computer_rolled_dice_value(self):
        if self.difficulty == "easy":
            easy_list_of_dice_values = [1,1,2,2,3,4,5,6]
            return random.choice(easy_list_of_dice_values)
        elif self.difficulty == "medium":
            return dice.Dice.roll()
        else:
            hard_list_of_dice_values = [1,2,3,4,4,5,5,6,6]
            return random.choice(hard_list_of_dice_values)