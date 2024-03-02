"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import random
import json
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
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
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
        scores = self.game.read_from_file("json_file.json")
        for player_stats in scores:

            player_name = player_stats.get("player_name")

            if name == player_name:
                print("Name already exists, choose another name")
                print("\n")
                return

        self.game.set_player_names(name)
        print(f"Name changed to {name}")

    def do_difficulty(self, arg):
        """Set a difficulty for the game."""
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            return
        if not arg:
            print("Difficulty was not provided. ", end="")
            print("Type 'difficulty' and the difficulty ",end="")
            print("afterwards please (easy, medium, hard)")

            return

        difficulty = arg.strip()
        if difficulty not in ("easy", "medium", "hard"):
            print(f"{arg} is not a valid difficulty level",end="")
            print("Provide either easy, medium or hard")
            return

        self.game.computer.set_computer_difficulty(difficulty)
        print(f"Difficulty changed to {difficulty}")
        print("You can now start to roll or hold or even cheat!")

    def do_roll(self, _):
        """Player rolls the dice."""
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty", end="")
            print("afterwards please (easy, medium, hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return

        dice_value = self.game.player_1.roll()
        x = self.game.player_rolls(dice_value)
        print("\n")
        print(f"{x[0]} rolled a {x[3]}")
        if x[4]:
            print(f"{x[0]} will gain 0 points")
            self._do_computer_plays_now()
        else:
            print(f"Your current round score is {x[1]}")
        print("\n")

    def do_hold(self, _):
        """Player holds."""
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty", end="")
            print("afterwards please (easy, medium, hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return

        x = self.game.player_holds()
        print(f"{x[0]} decided to hold.")
        print(f"Your score now is {x[1]}")
        print("\n")

        if not self.game.check_if_player_wins(self.game.player_1.score):
            self._do_computer_plays_now()
        else:
            y = self.game.get_player_info()
            print("Game is OVER")
            print(f"{y[0]} wins with a score of", end="")
            print(f"{y[1]} points in {y[2]}", end="")
            print(f"rounds at {y[3]} difficulty")

            if not self.game.cheats_used:
                self._do_write_into_file(self.game.player_1.name, self.game.player_1.score,
                self.game.player_1.num_rounds, self.game.computer.difficulty, "json_file.json")

    def do_exit(self, _):
        """Exit the game."""
        print("Thanks for playing! Goodbye!")
        return True

    def do_cheat(self, _):
        """Cheat in game to reach the game faster."""
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            return
        if self.game.computer.difficulty is None:
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty", end="")
            print("afterwards please (easy, medium, hard).")
            return
        if self.game.game_finished:
            print("Game is OVER. To start a new game type 'start'")
            return

        print("You decided to cheat. You will get 30 free points")
        z = self.game.player_cheats()

        print(f"Your score now is {z[0]}")

        if not self.game.check_if_player_wins(self.game.player_1.score):
            self._do_computer_plays_now()
        else:
            y = self.game.get_player_info()
            print("Game is OVER")
            print(f"{y[0]} wins with a score of", end="")
            print(f"{y[1]} points in {y[2]}", end="")
            print(f"rounds at {y[3]} difficulty")

            if not self.game.cheats_used:
                self._do_write_into_file(self.game.player_1.name, self.game.player_1.score,
                self.game.player_1.num_rounds, self.game.computer.difficulty, "json_file.json")

    def do_show(self, _):
        """Show player score and computer score."""
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return
        if self.game.player_1.name is None:
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            return

        name_scores = self.game.get_scores()
        print(f"Score of {name_scores[0]}: ({name_scores[1]})")
        print(f"Score of {name_scores[2]}: ({name_scores[3]})")

    def do_scores(self, _):
        """Read the scores from the file."""
        if self.game is None:
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            return

        print("Player statistics will be displayed", end="")
        print("in ascending order of rounds played.", end="")
        print("(The high score is determined by the fewest rounds played).")

        print("If you don't see your game here, you cheated or haven't played yet")

        scores = self.game.read_from_file("json_file.json")
        if scores is None:
            print("No games found yet")
        else:

            scores = sorted(scores, key=lambda x: x.get("num_rounds", float("inf")))

            for player_stats in scores:

                player_name = player_stats.get("player_name")
                player_score = player_stats.get("score")
                num_rounds = player_stats.get("num_rounds")
                difficulty = player_stats.get("difficulty")

                print(f"Player Name: {player_name}")
                print(f"Score: {player_score}")
                print(f"Number of Rounds: {num_rounds}")
                print(f"Difficulty: {difficulty}")
                print("\n")

    def do_default(self, _):
        """Start game with default settings."""
        print("\n")
        list_of_num = []
        self.do_start(self)
        n = random.randint(1, 100)
        while n in list_of_num:
            n = random.randint(1, 100)
        list_of_num.append(n)
        self.do_name("player" + str(n))
        self.do_difficulty("medium")
        print("\n")

    def _do_write_into_file(self, name, score, rounds, difficulty, filename):
        """Write Player Stats in File."""
        player_name = name
        player_score = score
        player_rounds = rounds
        player_difficulty = difficulty

        game_data = {
            "player_name": player_name,
            "score": player_score,
            "num_rounds": player_rounds,
            "difficulty": player_difficulty
        }

        try:
            with open(filename, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(game_data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4)

    def _do_computer_plays_now(self):
        print(f"{self.game.computer.name} plays now")
        computer_round = 0

        while True:
            choice = self.game.computer.return_decision_of_computer()
            if choice == "roll":
                computer_round += 1
                computer_dice_value = self.game.computer.return_computer_rolled_dice_value()
                print(f"{self.game.computer.name} rolled and got a {computer_dice_value}")
                if computer_dice_value == 1:
                    self.game.computer.num_rounds += 1
                    print(f"This means that {self.game.computer.name} gains 0 points in this round")
                    print(f"{self.game.computer.name}'s score is {self.game.computer.score}")
                    self.game.computer.current_round_score = 0
                    print("\n")
                    break

                self.game.computer.current_round_score += computer_dice_value
                print(f"{self.game.computer.name}'s current"
                f"round score is {self.game.computer.current_round_score}")

                if self.game.check_if_computer_wins(
                    self.game.computer.current_round_score, self.game.computer.score):
                    print(f"{self.game.computer.name} decided to hold.")
                    print(f"{self.game.computer.name} will gain", end="")
                    print(f"{self.game.computer.current_round_score} points")

                    print(f"{self.game.computer.name}'s score now is {self.game.computer.score}")
                    print("Game is OVER")
                    print(f"{self.game.computer.name} wins with a score"
                           f"of {self.game.computer.score} points in"
                    f"{self.game.computer.num_rounds}"
                      f"rounds at {self.game.computer.difficulty}"
                        f"difficulty")
                    break

            if choice == "hold" and computer_round == 0:
                computer_round += 1
                computer_dice_value = self.game.computer.return_computer_rolled_dice_value()
                print(f"{self.game.computer.name} rolled and got a {computer_dice_value}")
                if computer_dice_value == 1:
                    print(f"This means that {self.game.computer.name} gains 0 points in this round")
                    print(f"{self.game.computer.name}'s score is {self.game.computer.score}")
                    self.game.computer.current_round_score = 0
                    break

                self.game.computer.current_round_score += computer_dice_value
                print(f"{self.game.computer.name}'s current"
                       f"round score is {self.game.computer.current_round_score}")

                if self.game.check_if_computer_wins(
                    self.game.computer.current_round_score, self.game.computer.score):
                    print(f"{self.game.computer.name} decided"
                           f"to hold. {self.game.computer.name}"
                           f"will gain {self.game.computer.current_round_score} points")
                    print(f"{self.game.computer.name}'s"
                           f"score now is {self.game.computer.score}")
                    print("Game is OVER")
                    print(f"{self.game.computer.name} wins with"
                           f"a score of {self.game.computer.score} points"
                          f"in {self.game.computer.num_rounds} rounds"
                            f"at {self.game.computer.difficulty} difficulty")
                    break

            if choice == "hold":
                self.game.computer.num_rounds += 1
                self.game.computer.score += self.game.computer.current_round_score
                print(f"{self.game.computer.name} decided to hold.")
                print(f"{self.game.computer.name} gains", end="")
                print(f"{self.game.computer.current_round_score} points")
                print(f"{self.game.computer.name}'s score now is {self.game.computer.score}")
                self.game.computer.current_round_score = 0
                break
