import player, computer

class Game:
    def __init__(self) -> None:
        self.player_1 = player.Player()
        self.computer = computer.Computer()
        self.difficulty = None

    def set_player_names(self, player_name):
        self.player_1.name = player_name
        self.computer.name = "computer"

    