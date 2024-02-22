import cmd
from game import Game

class Shell(cmd.Cmd):

    intro = "\nWelcome to Pig Dice Game. Type help or ? to list commands\n"

    prompt = "(game) "

    def __init__(self):
        super().__init__()
        
        self.game = None
    
    def do_start(self, _):
        "start a brand new game"
        self.game = Game()
        print("New game started")

    def do_name(self, arg):
        "set a new name for the player"
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if not arg:
            print("Name was not provided. Type 'name' and your name afterwards please (e.g. name Larsson)")
            return
        
        name = arg.strip()
        self.game.set_player_names(name)
        print(f"Name changed to {name}")

    def do_difficulty(self, arg):
        "set a difficulty for the game"
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print(f"Please provide a name first. Type 'name' and your name afterwards please (e.g. name Patrick).")
            return
        if not arg:
            print("Difficulty was not provided. Type 'difficulty' and the difficulty afterwards please (easy,medium,hard)")
            return
        
        difficulty = arg.strip()
        if difficulty != "easy" and difficulty!= "medium" and difficulty!= "hard":
            print(f"{arg} is not a valid difficulty level. Provide either easy, medium or hard")
            return
        
        self.game.computer.set_computer_difficulty(difficulty)
        print(f"Difficulty changed to {difficulty}")
        print(f"You can now start to roll or hold!")
        