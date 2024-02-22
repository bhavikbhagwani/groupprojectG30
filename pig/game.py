import player, computer, dice

class Game:
    def __init__(self) -> None:
        self.player_1 = player.Player()
        self.computer = computer.Computer()
        self.difficulty = None
        self.dice = dice.Dice()

    def set_player_names(self, player_name):
        self.player_1.name = player_name
        self.computer.name = "computer"
    

    def player_rolls(self):
        dice_value = self.dice.roll()
        print(f"{self.player_1.name} rolled a {dice_value}")

        if dice_value == 1:
            print(f"This means that {self.player_1.name} gains 0 points in this round")
            self.player_1.current_round_score = 0
        
        else:#if doesnt roll a 1
            self.player_1.current_round_score += dice_value
            print(f"{self.player_1.name}'s current round score is {self.player_1.current_round_score}")

     
    