

"""Unit testing."""

import json
import random
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import dice
import computer
import player
import game


class TestDiceClass(unittest.TestCase):  # noqa: H601
    """Test the Dice Class."""

    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""

        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    

class TestComputerClass(unittest.TestCase):
    """Test the Computer Class."""

    def test_setting_difficulty(self):
        """Set difficulty and test if either easy,medium or hard."""
        computer_test = computer.Computer()

        example_difficulty = random.choice(["easy","medium","hard"])
        
        res = computer_test.set_computer_difficulty(example_difficulty)
        self.assertEqual(res, example_difficulty)

    def test_roll_a_dice_for_computer(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()

        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_decision_return_for_computer(self):
        """Decision for computer."""
        computer_test = computer.Computer()

        
        res = computer_test.return_decision_of_computer()

        self.assertTrue(res in ["roll","hold"])

    

class TestPlayerClass(unittest.TestCase):
    """Test the Player Class."""

    def test_roll_a_dice_for_player(self):
        """Roll a dice and check value is in bounds."""
        player_test = player.Player()

        res = player_test.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

class TestGameClass(unittest.TestCase):
    """Test the Game Class."""

    def test_get_correct_name(self):
        """Roll a dice and check value is in bounds."""

        game_test = game.Game()
        name = "Larsson"
        res = game_test.set_player_names(name)
        exp = name
        self.assertEqual(res,exp)
    
    def test_check_if_player_wins(self):
        """Player wins test."""
        game_test = game.Game()

        res = game_test.check_if_player_wins(51)
        self.assertTrue(res)

    def test_check_if_computer_wins(self):
        """Computer wins test."""
        game_test = game.Game()

        res = game_test.check_if_computer_wins(2,49)
        self.assertTrue(res)
    
    def test_player_cheats(self):
        """Cheat and check the modifications"""
        game_test = game.Game()
        current_num_rounds = game_test.player_1.num_rounds
        current_score = game_test.player_1.score
        # Act: Call the method you want to test
        game_test.player_cheats()

        # Assert: Check the expected results
        self.assertTrue(game_test.cheats_used)  # Assert that cheats_used is set to True
        self.assertGreater(game_test.player_1.num_rounds, current_num_rounds)  # Assert that num_rounds is incremented
        self.assertGreater(game_test.player_1.score, current_score)  # Assuming the current_round_score is added to the score
        self.assertEqual(game_test.player_1.current_round_score, 0)  # Assuming it's reset after cheating
        # You can add more assertions based on your game logic
    
    def test_write_into_file(self):
        """Test writing Player Stats into File."""

        game_instance = game.Game()
        game_instance.write_into_file("example-name",100,1000000,"easy")

        # Add your assertions here, for example:
        with open("json_file.json", "r", encoding="utf-8") as file:
            data_written = json.load(file)

        # Check if the expected data is in the file
        self.assertIn({"player_name": "example-name", "score": 100, "num_rounds": 1000000, "difficulty": "easy"}, data_written)

    

if __name__ == "__main__":
    unittest.main()
