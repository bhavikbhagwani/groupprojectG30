"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import random
import json
from game import Game
import highscore
import histogram


class Shell(cmd.Cmd):
    """Example of Shell Class."""

    intro = "\nWelcome to Pig Dice Game. Type help or ? to list commands\n"

    prompt = "(game) "

    def __init__(self):
        """Init Shell."""
        super().__init__()

        self.game = None

    def do_rules(self, _):
        """Display Rules Of Game."""
        print("\n")
        print("Lets play the Pig Dice Game Normal Variation 50 points")
        print("")
        print("You will play against the computer. ", end="")
        print("You will roll the dice and the dice value")
        print("gets added to your score.")
        print("")
        print("But be careful, if you get a one on the dice, you lose all the")
        print("current points you accumulated")
        print("")
        print("To start, first start the game using 'start' then")
        print("change your name typing 'name' followed by your name and then")
        print("set the difficulty typing 'difficulty' followed")
        print("by the difficulty (easy, medium, hard)")
        print("OR type 'default' to start quick ", end="")
        print("and play with default settings")
        print("")
        print("Play at your own risk. Good Luck!")
        print("\n")

    def do_start(self, _):
        """Start a brand new game."""
        print("\n")
        self.game = Game()
        print("New game started")
        print("\n")

    def do_name(self, arg):
        """Set a new name for the player."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.game_finished:
            print("\n")
            print("Game is OVER. To start a new game type 'start'")
            print("\n")
            return
        if not arg:
            print("\n")
            print("Name was not provided. Type 'name'"
                  "and your name afterwards please (e.g. name Larsson)")
            print("\n")
            return

        print("\n")
        name = arg.strip()
        h_s = highscore.HighScore()
        scores = h_s.read_from_file("json_file.json")
        for player_stats in scores:

            player_name = player_stats.get("player_name")

            if name == player_name:
                print("Name already exists, choose another name")
                print("\n")
                return

        self.game.set_player_names(name)
        print(f"Name changed to {name}")
        print("\n")

    def do_difficulty(self, arg):
        """Set a difficulty for the game."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.game_finished:
            print("\n")
            print("Game is OVER. To start a new game type 'start'")
            print("\n")
            return
        if self.game.player_1.name is None:
            print("\n")
            print("Name not set yet")
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            print("\n")
            return
        if not arg:
            print("\n")
            print("Difficulty was not provided. ", end="")
            print("Type 'difficulty' and the difficulty ", end="")
            print("afterwards please (easy, medium, hard)")
            print("\n")
            return

        difficulty = arg.strip()
        if difficulty not in ("easy", "medium", "hard"):
            print("\n")
            print(f"{arg} is not a valid difficulty level", end="")
            print("Provide either easy, medium or hard")
            print("\n")
            return

        print("\n")
        self.game.computer.set_computer_difficulty(difficulty)
        print(f"Difficulty changed to {difficulty}")
        print("\n")
        print("You can now start to roll or hold or even cheat!")
        print("\n")

    def do_roll(self, _):
        """Player rolls the dice."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.player_1.name is None:
            print("\n")
            print("Name not set yet")
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            print("\n")
            return
        if self.game.computer.difficulty is None:
            print("\n")
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty ", end="")
            print("afterwards please (easy, medium, hard).")
            print("\n")
            return
        if self.game.game_finished:
            print("\n")
            print("Game is OVER. To start a new game type 'start'")
            print("\n")
            return

        dice_value = self.game.player_1.roll()
        x = self.game.player_rolls(dice_value)
        print("\n")
        print(f"{x[0]} rolled a ({x[3]})")
        if x[4]:
            print(f"{x[0]} will gain 0 points")
            print("\n")
            self._do_computer_plays_now()
        else:
            print(f"Your current round score is {x[1]}")
        print("\n")

    def do_hold(self, _):
        """Player holds."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.player_1.name is None:
            print("\n")
            print("Name not set yet")
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            print("\n")
            return
        if self.game.computer.difficulty is None:
            print("\n")
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty", end="")
            print("afterwards please (easy, medium, hard).")
            print("\n")
            return
        if self.game.game_finished:
            print("\n")
            print("Game is OVER. To start a new game type 'start'")
            print("\n")
            return

        x = self.game.player_holds()
        print("\n")
        print(f"{x[0]} decided to hold.")
        print(f"Your score now is ({x[1]})")
        print("\n")

        if not self.game.check_if_player_wins(self.game.player_1.score):
            self._do_computer_plays_now()
        else:
            y = self.game.get_player_info()
            print("Game is OVER")
            print("\n")
            print(f"{y[0]} wins with a score of ", end="")
            print(f"{y[1]} points in {y[2]} ", end="")
            print(f"rounds at {y[3]} difficulty")
            print("\n")

            if not self.game.cheats_used:
                self._do_write_histogram()
                print("PLAYER HISTOGRAM FREQUENCY STORED. ", end="")
                print("TYPE 'histogram' TO SEE.")
                self._do_write_into_file(
                    self.game.player_1.name,
                    self.game.player_1.score,
                    self.game.player_1.num_rounds,
                    self.game.computer.difficulty,
                    "json_file.json"
                )
                print("PLAYER STATS STORED IN HIGH SCORE LIST. ", end="")
                print("TYPE 'scores' TO SEE.")
                print("\n")

    def do_exit(self, _):
        """Exit the game."""
        print("\n")
        print("Thanks for playing! Goodbye!")
        print("\n")
        return True

    def do_cheat(self, _):
        """Cheat in game to reach the game faster."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.player_1.name is None:
            print("\n")
            print("Name not set yet")
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            print("\n")
            return
        if self.game.computer.difficulty is None:
            print("\n")
            print("Difficulty is not yet set. ", end="")
            print("Type 'difficulty' and the difficulty", end="")
            print("afterwards please (easy, medium, hard).")
            print("\n")
            return
        if self.game.game_finished:
            print("\n")
            print("Game is OVER. To start a new game type 'start'")
            print("\n")
            return

        print("\n")
        print("You decided to cheat. You will get 30 free points")
        z = self.game.player_cheats()

        print(f"Your score now is {z[0]}")

        if not self.game.check_if_player_wins(self.game.player_1.score):
            self._do_computer_plays_now()
        else:
            y = self.game.get_player_info()
            print("\n")
            print("Game is OVER")
            print("\n")
            print(f"{y[0]} wins with a score of ", end="")
            print(f"{y[1]} points in {y[2]} ", end="")
            print(f"rounds at {y[3]} difficulty")
            print("\n")

            if not self.game.cheats_used:
                self._do_write_histogram()
                print("PLAYER HISTOGRAM FREQUENCY STORED. ", end="")
                print("TYPE 'histogram' TO SEE.")
                self._do_write_into_file(
                    self.game.player_1.name,
                    self.game.player_1.score,
                    self.game.player_1.num_rounds,
                    self.game.computer.difficulty,
                    "json_file.json"
                )
                print("PLAYER STATS STORED IN HIGH SCORE LIST. ", end="")
                print("TYPE 'scores' TO SEE.")
                print("\n")

    def do_show(self, _):
        """Show player score and computer score."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        if self.game.player_1.name is None:
            print("\n")
            print("Type 'name' and your name afterwards please. ", end="")
            print("(e.g. name Patrick).")
            print("\n")
            return

        name_scores = self.game.get_scores()
        print("\n")
        print(f"Score of {name_scores[0]}: ({name_scores[1]})")
        print(f"Score of {name_scores[2]}: ({name_scores[3]})")
        print("\n")

    def do_scores(self, _):
        """Read the scores from the file."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return

        print("\n")
        print("Player statistics will be displayed ", end="")
        print("in ascending order of rounds played.", end="")
        print(" and difficulty (hard -> easy) ", end="")
        print("(The high score is determined by the ", end="")
        print("fewest rounds played and by difficulty)")

        print("If you don't see your game here, ", end="")
        print("you cheated or haven't played yet")

        h_s = highscore.HighScore()
        scores = h_s.read_from_file("json_file.json")
        if len(scores) == 0:
            print("No games found yet")
            print("\n")
        else:

            scores = sorted(
                scores,
                key=lambda x: (
                    {"easy": 2, "medium": 1, "hard": 0}.get(
                        x.get("difficulty", "hard")),
                    x.get(
                        "num_rounds", float("inf"))
                )
            )

            print("HIGH SCORE LIST\n")

            for i, scores in enumerate(scores, start=1):
                print("NUMBER " + str(i))
                print("")
                player_name = scores.get("player_name")
                player_score = scores.get("score")
                num_rounds = scores.get("num_rounds")
                difficulty = scores.get("difficulty")

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
        self.do_name("player" + "_" + str(n))
        self.do_difficulty("medium")
        print("\n")

    def _do_write_into_file(self, name, score, rounds, difficulty, filename):

        h_s = highscore.HighScore()
        h_s.set_info(name, score, rounds, difficulty)
        h_s.write_into_file(filename)

    def _do_write_histogram(self):
        hist = histogram.Histogram()
        hist.set_info(
            self.game.player_1.name, self.game.player_1.frequency
            )
        hist.write_into_file("histogram.json")

    def _do_computer_plays_now(self):
        print(f"{self.game.computer.name} plays now")
        print("")
        computer_round = 0

        while True:
            choice = self.game.computer.return_decision_of_computer()
            if choice == "roll":
                computer_round += 1
                c_d_v = self.game.computer.return_computer_rolled_dice_value()
                print(f"{self.game.computer.name} rolled and got a ({c_d_v})")
                print("\n")
                if c_d_v == 1:
                    self.game.computer.num_rounds += 1
                    print("This means that  ", end="")
                    print(f"{self.game.computer.name} ", end="")
                    print("gains 0 points in this round")
                    print(f"{self.game.computer.name}'s ", end="")
                    print(f"score is ({self.game.computer.score})")
                    self.game.computer.current_round_score = 0
                    print("\n")
                    break

                self.game.computer.current_round_score += c_d_v
                print(f"{self.game.computer.name}'s current ", end="")
                print("round score is ", end="")
                print(f"{self.game.computer.current_round_score}")
                print("\n")

                if self.game.check_if_computer_wins(
                    self.game.computer.current_round_score,
                    self.game.computer.score
                ):
                    print(f"{self.game.computer.name} decided to hold.")
                    print(f"{self.game.computer.name} will gain", end="")
                    print(f"{self.game.computer.current_round_score} points")

                    print(f"{self.  game.computer.name}'s ", end="")
                    print(f"score now is ({self.game.computer.score})")
                    print("Game is OVER")
                    print(f"{self.game.computer.name} wins ", end="")
                    print("with a score ", end="")
                    print(f"of {self.game.computer.score} points in ", end="")
                    print(f"{self.game.computer.num_rounds} ", end="")
                    print("rounds at ", end="")
                    print(f"{self.game.computer.difficulty} ")
                    print("difficulty")
                    print("\n")
                    break

            if choice == "hold" and computer_round == 0:
                computer_round += 1
                c_d_v = self.game.computer.return_computer_rolled_dice_value()
                print(f"{self.game.computer.name} rolled and got a ({c_d_v})")
                print("\n")
                if c_d_v == 1:
                    print("This means that  ", end="")
                    print(f"{self.game.computer.name} ", end="")
                    print("gains 0 points in this round")
                    print(f"{self.game.computer.name}'s score ", end="")
                    print(f"is ({self.game.computer.score})")
                    self.game.computer.current_round_score = 0
                    break

                self.game.computer.current_round_score += c_d_v
                print(f"{self.game.computer.name}'s current ", end="")
                print("round score is ", end="")
                print(f"{self.game.computer.current_round_score}")

                if self.game.check_if_computer_wins(
                    self.game.computer.current_round_score,
                    self.game.computer.score
                ):
                    print(f"{self.game.computer.name} decided to hold.")
                    print(f"{self.game.computer.name} will gain", end="")
                    print(f"{self.game.computer.current_round_score} points")

                    print(f"{self.game.computer.name}'s ", end="")
                    print(f"score now is ({self.game.computer.score})")
                    print("Game is OVER")
                    print(f"{self.game.computer.name} wins ", end="")
                    print("with a score ", end="")
                    print(f"of {self.game.computer.score} points in ", end="")
                    print(f"{self.game.computer.num_rounds} ", end="")
                    print("rounds at ", end="")
                    print(f"{self.game.computer.difficulty} ")
                    print("difficulty")
                    print("\n")
                    break

            if choice == "hold":
                self.game.computer.num_rounds += 1
                self.game.computer.score += (
                    self.game.computer.current_round_score
                )
                print(f"{self.game.computer.name} decided to hold.")
                print(f"{self.game.computer.name} gains ", end="")
                print(f"{self.game.computer.current_round_score} points")
                print("\n")
                print(f"{self.game.computer.name}'s score now ", end="")
                print(f"is ({self.game.computer.score})")
                print("\n")
                self.game.computer.current_round_score = 0
                break

    def do_histogram(self, _):
        """Show Histogram For Players."""
        if self.game is None:
            print("\n")
            print("Please start a new game first. ", end="")
            print("You can do this by typing 'start'")
            print("You can also type 'default' to start the game faster")
            print("\n")
            return
        print("\n")
        hist = histogram.Histogram()
        histogram_data = hist.read_histogram("histogram.json")

        if len(histogram_data) == 0:
            print("\n")
            print("No games found yet")
            print("\n")
        else:

            for entry in histogram_data:

                player_name = entry["player_name"]
                histogram_map = entry["hist"]
                print("Histogram frequency ", end="")
                print(f"for {player_name}")

                for dice_value, frequency in histogram_map.items():
                    print(f"{dice_value}: {'*' * frequency}")

                print("\n" + "=" * 30 + "\n")
