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