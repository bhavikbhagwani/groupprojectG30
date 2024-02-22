import player

class Game:
    def __init__(self) -> None:
        self.player_1 = player.Player()
        self.player_2 = player.Player()

    def set_player_names(self, player_name):
        self.player_1.name = player_name
        self.player_2.name = "computer"