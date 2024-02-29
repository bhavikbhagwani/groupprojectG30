"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import random
from game import Game


class Shell(cmd.Cmd):
    """Example of Shell Class."""

    intro = "\nWelcome to Pig Dice Game. Type help or ? to list commands\n"

    prompt = "(game) "

    def __init__(self):
        """Init Shell."""
        super().__init__()

        self.game = None

    def do_start(self, _):
        """Start a brand new game."""
        self.game = Game()
        print("New game started")

    def do_name(self, arg):
        """Set a new name for the player."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return
        if not arg:
            print("Name was not provided. Type 'name'"
                  "and your name afterwards please (e.g. name Larsson)")
            return

        name = arg.strip()
        self.game.set_player_names(name)
        print(f"Name changed to {name}")

    def do_difficulty(self, arg):
        """Set a difficulty for the game."""
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Please provide a name first. Type 'name'"
                  "and your name afterwards please (e.g. name Patrick).")
            return
        if not arg:
            print("Difficulty was not provided. Type 'difficulty'"
                  "and the difficulty afterwards please (easy,medium,hard)")
            return

        difficulty = arg.strip()
        if difficulty not in ("easy", "medium", "hard"):
            print(f"{arg} is not a valid difficulty level. Provide either easy, medium or hard")
            return

        self.game.computer.set_computer_difficulty(difficulty)
        print(f"Difficulty changed to {difficulty}")
        print("You can now start to roll or hold or even cheat!")

    def do_roll(self, _):
        """Player rolls the dice."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Please provide a name first. Type 'name'"
                  "and your name afterwards please (e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. Type 'difficulty'"
                   "and the difficulty afterwards please (easy,medium,hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return

        self.game.player_rolls()

    def do_hold(self, _):
        """Player holds."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Please provide a name first. Type 'name'"
                  "and your name afterwards please (e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. Type 'difficulty'"
                   "and the difficulty afterwards please (easy,medium,hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return

        self.game.player_holds()

    def do_exit(self, _):
        """Exit the game."""
        print("Thanks for playing! Goodbye!")
        return True

    def do_cheat(self, _):
        """Cheat in game to reach the game faster."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Please provide a name first. Type 'name'"
                  "and your name afterwards please (e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. Type 'difficulty'"
                   "and the difficulty afterwards please (easy,medium,hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return
        self.game.player_cheats()

    def do_show(self, _):
        """Show player score and computer score."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Please provide a name first. Type 'name'"
                  "and your name afterwards please (e.g. name Patrick).")
            return

        print(f"Score of {self.game.player_1.name}: ({self.game.player_1.score})")
        print(f"Score of computer: ({self.game.computer.score})")

    def do_scores(self, _):
        """Read the scores from the file."""
        if self.game is None:
            print("Please start a new game first. You can do this by typing 'start'")
            return
        self.game.read_from_file()

    def do_default(self, _):
        """Start game with default settings."""
        list_of_num = []
        self.do_start(self)
        n = random.randint(1, 100)
        while n in list_of_num:
            n = random.randint(1, 100)
        list_of_num.append(n)
        self.do_name("player" + str(n))
        self.do_difficulty("medium")
