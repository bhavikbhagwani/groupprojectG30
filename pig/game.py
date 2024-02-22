import player, computer, dice, random

class Game:
    def __init__(self):
        self.player_1 = player.Player()
        self.computer = computer.Computer()
        self.difficulty = None
        self.dice = dice.Dice()
        self.roll_or_hold_list_computer = ["roll","roll","hold"]

    def set_player_names(self, player_name):
        self.player_1.name = player_name
        self.computer.name = "computer"
    

    def player_rolls(self):
        dice_value = self.dice.roll()
        print(f"{self.player_1.name} rolled a {dice_value}")

        if dice_value == 1:
            print(f"This means that {self.player_1.name} gains 0 points in this round")
            self.player_1.current_round_score = 0
            
            self.computer_plays()
        
        else:#if doesnt roll a 1
            self.player_1.current_round_score += dice_value
            print(f"{self.player_1.name}'s current round score is {self.player_1.current_round_score}")

    
    def player_holds(self):
        self.player_1.score += self.player_1.current_round_score
        print(f"{self.player_1.name} decided to hold. {self.player_1.name} will gain {self.player_1.current_round_score} points")
        print(f"Your score now is {self.player_1.score}")
        self.player_1.current_round_score = 0

        if self.player_1.score >= 50:
            print("Game is OVER")
            print(f"{self.player_1.name} wins with a score of {self.player_1.score} points")
        
        self.computer_plays()

    def computer_plays(self):
        print(f"{self.computer.name} plays now")
        while True:
            choice = random.choice(self.roll_or_hold_list_computer)
            if choice == "roll":
                computer_dice_value = self.computer.return_computer_rolled_dice_value()
                print(f"{self.computer.name} rolled and got a {computer_dice_value}")
                if computer_dice_value == 1:
                    print(f"This means that {self.computer.name} gains 0 points in this round")
                    print(f"{self.computer.name}'s score is {self.computer.score}")
                    self.computer.current_round_score = 0
                    break
                else:#dice value is not 1
                    self.computer.current_round_score += computer_dice_value
                    print(f"{self.computer.name}'s current round score is {self.computer.current_round_score}")
            
            if choice == "hold":
                self.computer.score += self.computer.current_round_score
                print(f"{self.computer.name} decided to hold. {self.computer.name} gains {self.computer.current_round_score} points ")
                print(f"{self.computer.name}'s score now is {self.computer.score}")
                self.computer.current_round_score = 0
                break