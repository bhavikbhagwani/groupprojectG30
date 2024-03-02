"""
Game class.

This is where all the game takes place
It instantiates the Game with its corresponding properties
and is responsible for all the shell commands in the shell.py
This is like the heart of the program
"""

import json
import player
import computer
import dice


class Game:
    """Example of Game Class."""

    def __init__(self):
        """Init method of the Game."""
        self.player_1 = player.Player()
        self.computer = computer.Computer()
        self.difficulty = None
        self.dice = dice.Dice()
        self.max_score = 50
        self.game_finished = False
        self.cheats_used = False

    def set_player_names(self, player_name):
        """Set name for Player."""
        self.player_1.name = player_name
        self.computer.name = "computer"
        return self.player_1.name

    def player_rolls(self, dice_value):
        """Player decides to Roll."""
        round_lost = False
        

        if dice_value == 1:
            self.player_1.num_rounds += 1
            self.player_1.current_round_score = 0
            round_lost = True
            

        else:
            self.player_1.current_round_score += dice_value
        
        return [self.player_1.name, self.player_1.current_round_score, self.player_1.score, dice_value, round_lost]

    def player_holds(self):
        """Player decides to Hold."""
        self.player_1.num_rounds += 1
        self.player_1.score += self.player_1.current_round_score
        self.player_1.current_round_score = 0

        return [self.player_1.name, self.player_1.score,self.player_1.current_round_score,self.player_1.num_rounds]

        

    def check_if_computer_wins(self, current_round_score, score):
        """Check if Computer has Won."""
        if score + current_round_score >= self.max_score:
            self.computer.score += self.computer.current_round_score
            self.game_finished = True
            return True
        return False

    def check_if_player_wins(self, score):
        """Check if the Player has Won."""
        if score >= self.max_score:
            self.game_finished = True
            return True
        return False

    def player_cheats(self):
        """Player cheats in Game."""
        self.cheats_used = True
        self.player_1.num_rounds += 1
        self.player_1.score += 30
        self.player_1.current_round_score = 0

        return [self.player_1.score,self.player_1.current_round_score,self.player_1.num_rounds,self.cheats_used]

    def get_scores(self):
        return [self.player_1.name,self.player_1.score,self.computer.name,self.computer.score]   

    def get_player_info(self):
        list = [self.player_1.name, self.player_1.score,self.player_1.num_rounds,self.computer.difficulty]
        return list
    

    def read_from_file(self, filename):
        """Read Player Stats from File."""
        print("\n")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                scores = json.load(file)
        except FileNotFoundError:
            scores = []

        return scores
