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