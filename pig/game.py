import player

class Game:
    def __init__(self) -> None:
        self.player_1 = player.Player()
        self.player_2 = player.Player()
        self.difficulty = None

    def set_player_names(self, player_name):
        self.player_1.name = player_name
        self.player_2.name = "computer"

    def set_game_difficulty(self, difficulty):
        self.difficulty = difficulty