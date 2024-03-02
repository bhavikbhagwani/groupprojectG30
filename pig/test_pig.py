

"""Unit testing."""

import os
import json
import tempfile
import random
import unittest
import dice
import computer
import player
import game


class TestDiceClass(unittest.TestCase):

    def test_init_default_object(self):

        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res,exp)
    
    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)
    
class TestComputerClass(unittest.TestCase):
    """Test the Computer Class."""

    def test_setting_difficulty(self):
        """Set difficulty and test if either easy,medium or hard."""
        computer_test = computer.Computer()

        example_difficulty = random.choice(["easy", "medium", "hard"])

        res = computer_test.set_computer_difficulty(example_difficulty)
        self.assertEqual(res, example_difficulty)

    def test_roll_a_dice_for_computer_easy(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()
        computer_test.set_computer_difficulty("easy")
        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)
    def test_roll_a_dice_for_computer_medium(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()
        computer_test.set_computer_difficulty("medium")
        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_roll_a_dice_for_computer_hard(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()
        computer_test.set_computer_difficulty("hard")
        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_decision_return_for_computer(self):
        """Decision for computer."""
        computer_test = computer.Computer()

        res = computer_test.return_decision_of_computer()

        self.assertTrue(res in ["roll", "hold"])

class TestPlayerClass(unittest.TestCase):
    """Test the Computer Class."""

    def test_roll_of_player(self):
        """Set difficulty and test if either easy,medium or hard."""
        player_test = player.Player()

        res = player_test.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)


class TestGameClass(unittest.TestCase):

    def test_init_default_object(self):

        game_test = game.Game()
        self.assertIsInstance(game_test, game.Game)
    
    def test_get_correct_name(self):
        """Roll a dice and check value is in bounds."""
        game_test = game.Game()
        name = "Larsson"
        res = game_test.set_player_names(name)
        exp = name
        self.assertEqual(res, exp)

    def test_player_roll_dice_1(self):
        game_test = game.Game()
        current_round_score_before = game_test.player_1.current_round_score
        list_of_values = game_test.player_rolls(1)

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        
        self.assertTrue(list_of_values[4])
        
            
    
    def test_player_roll_dice_not_1(self):
        game_test = game.Game()
        current_round_score_before = game_test.player_1.current_round_score
        list_of_values = game_test.player_rolls(4)

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertFalse(list_of_values[4])
        self.assertGreater(list_of_values[1],current_round_score_before)
    
    def test_player_holds(self):
        game_test = game.Game()
        num_rounds_before = game_test.player_1.num_rounds
        list_of_values = game_test.player_holds()
        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.num_rounds, list_of_values)

        self.assertGreater(list_of_values[3],num_rounds_before)

    def test_roll_and_hold(self):
        game_test = game.Game()
        
        list_of_values = game_test.player_rolls(5)
        name_before = list_of_values[0]
        c_r_s_before = list_of_values[1]
        score_before = list_of_values[2]

        list_of_values_2 = game_test.player_holds()
        self.assertEqual(name_before,list_of_values_2[0])
        self.assertGreater(list_of_values_2[1],score_before)
        self.assertLess(list_of_values_2[2],c_r_s_before)

    
    def test_player_cheats(self):
        game_test = game.Game()

        cheats_used_before = game_test.cheats_used
        num_rounds_before = game_test.player_1.num_rounds
        score_before = game_test.player_1.score


        list_of_values = game_test.player_cheats()
        score = list_of_values[0]
        cheats_used = list_of_values[3]
        num_rounds = list_of_values[2]

        self.assertTrue(cheats_used)
        self.assertNotEqual(cheats_used_before,cheats_used)
        self.assertGreater(num_rounds,num_rounds_before)
        self.assertGreater(score,score_before)
    
    def test_getting_scores(self):
        game_test = game.Game()

        list_of_values = game_test.get_player_info()

        self.assertIn(game_test.player_1.name,list_of_values)
        self.assertIn(game_test.player_1.score,list_of_values)
        self.assertIn(game_test.player_1.num_rounds,list_of_values)
        self.assertIn(game_test.computer.difficulty, list_of_values)
    
    def test_scores_getting(self):
        game_test = game.Game()
        list_of_values = game_test.get_scores()

        self.assertIn(game_test.player_1.name,list_of_values)
        self.assertIn(game_test.player_1.score,list_of_values)
        self.assertIn(game_test.computer.name,list_of_values)
        self.assertIn(game_test.computer.score, list_of_values)

    def test_check_if_player_wins_true(self):
        """Player wins test."""
        game_test = game.Game()

        res = game_test.check_if_player_wins(51)
        self.assertTrue(res)
    
    def test_check_if_player_wins_false(self):
        """Player wins test."""
        game_test = game.Game()

        res = game_test.check_if_player_wins(45)
        self.assertFalse(res)

    def test_check_if_computer_wins_true(self):
        """Computer wins test."""
        game_test = game.Game()

        res = game_test.check_if_computer_wins(2, 49)
        self.assertTrue(res)   

    def test_check_if_computer_wins_false(self):
        """Computer wins test."""
        game_test = game.Game()

        res = game_test.check_if_computer_wins(4, 30)
        self.assertFalse(res)

    def test_reading_scores_from_file(self):
        
        game_test = game.Game()
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as temp_file:
            temp_filename = temp_file.name
            game_data = {
            "player_name": "player_name",
            "score": "player_score",
            "num_rounds": "player_rounds",
            "difficulty": "player_difficulty"
        }
            json.dump([game_data], temp_file)

        try:
            # Call your method with the temporary file name
            scores = game_test.read_from_file(temp_filename)

            # Check if scores is a list
            self.assertIsInstance(scores, list)

        finally:
            # Remove the temporary file
            os.remove(temp_filename)
    
    def test_reading_scores_from_not_existing_file(self):
        
        game_test = game.Game()
        
        scores = game_test.read_from_file("non-existing.json")
        self.assertEqual(len(scores),0)


if __name__ == "__main__":
    unittest.main()
