
class Computer:
    def __init__(self):
        self.name = "computer"
        self.score = 0
        self.current_round_score = 0
        self.difficulty = None
    
    def set_computer_difficulty(self, difficulty):
        self.difficulty = difficulty
    