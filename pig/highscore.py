"""
High Score class.

This class instantiates a HighScore
and contains some methods to read and write scores into/from file
"""

import json

class HighScore:
    def __init__(self):
        """Init HighScore."""
        self.name = None
        self.score = None
        self.num_rounds = None
        self.difficulty = None
    
    def set_info(self, name, score, num_rounds, difficulty):
        """Setting info to write into file."""
        self.name = name
        self.score = score
        self.num_rounds = num_rounds
        self.difficulty = difficulty
    
    def write_into_file(self, filename):
        """Write Player Stats in File."""
        player_name = self.name
        player_score = self.score
        player_rounds = self.num_rounds
        player_difficulty = self.difficulty

        game_data = {
            "player_name": player_name,
            "score": player_score,
            "num_rounds": player_rounds,
            "difficulty": player_difficulty
        }


        try:
            with open(filename, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(game_data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4)
        
        return game_data
    
    def read_from_file(self, filename):
        """Read Player Stats from File."""
        print("\n")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                scores = json.load(file)
        except FileNotFoundError:
            scores = []

        return scores
    