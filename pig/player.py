
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
    
    def roll(self):
        return self.player_dice.roll()
