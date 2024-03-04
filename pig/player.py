
"""
Player class.

This class instantiates a Player
"""
import dice


class Player:
    """Example of Player class."""

    def __init__(self):
        """Init method."""
        self.name = None
        self.score = 0
        self.current_round_score = 0
        self.num_rounds = 0
        self.player_dice = dice.Dice()
        self.frequency = [0, 0, 0, 0, 0, 0]

    def roll(self):
        """Return rolling value from player."""
        dice_value = self.player_dice.roll()
        if dice_value == 1:
            self.frequency[0] += 1
        elif dice_value == 2:
            self.frequency[1] += 1
        elif dice_value == 3:
            self.frequency[2] += 1
        elif dice_value == 4:
            self.frequency[3] += 1
        elif dice_value == 5:
            self.frequency[4] += 1
        else:
            self.frequency[5] += 1
        
        return dice_value
