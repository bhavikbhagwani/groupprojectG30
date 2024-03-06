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
        x = []
        x.append(self.player_1.name)
        x.append(self.player_1.current_round_score)
        x.append(self.player_1.score)
        x.append(dice_value)
        x.append(round_lost)
        return x

    def player_holds(self):
        """Player decides to Hold."""
        self.player_1.num_rounds += 1
        self.player_1.score += self.player_1.current_round_score
        self.player_1.current_round_score = 0

        x = []
        x.append(self.player_1.name)
        x.append(self.player_1.score)
        x.append(self.player_1.current_round_score)
        x.append(self.player_1.num_rounds)
        return x

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

        x = []
        x.append(self.player_1.score)
        x.append(self.player_1.current_round_score)
        x.append(self.player_1.num_rounds)
        x.append(self.cheats_used)
        return x

    def get_scores(self):
        """Return scores player & computer."""
        x = []
        x.append(self.player_1.name)
        x.append(self.player_1.score)
        x.append(self.computer.name)
        x.append(self.computer.score)
        return x

    def get_player_info(self):
        """Return player info for printing."""
        x = []
        x.append(self.player_1.name)
        x.append(self.player_1.score)
        x.append(self.player_1.num_rounds)
        x.append(self.computer.difficulty)
        return x

    def read_histogram(self, filename):
        """Read histogram frequency from File."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                histogram_data = json.load(file)
        except FileNotFoundError:
            histogram_data = []

        return histogram_data
