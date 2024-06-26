

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
import highscore
import histogram


class TestDiceClass(unittest.TestCase):
    """Test the Dice Class."""

    def test_init_default_object(self):
        """Test Init of Dice."""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)


class TestComputerClass(unittest.TestCase):
    """Test the Computer Class."""

    def test_init_default_object(self):
        """Test Init of Computer."""
        computer_test = computer.Computer()
        self.assertIsInstance(computer_test, computer.Computer)

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

    def test_init_default_object(self):
        """Test Init of Player."""
        player_test = player.Player()
        self.assertIsInstance(player_test, player.Player)

    def test_roll_of_player(self):
        """Testing roll of player."""
        player_test = player.Player()

        res = player_test.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_roll_of_player_frequency(self):
        """Testing increase of frequency when dice rolled."""
        player_test = player.Player()
        freq_list = player_test.frequency
        dice_value = player_test.roll()
        if dice_value == 1:
            self.assertEqual(freq_list[0], 1)
        elif dice_value == 2:
            self.assertEqual(freq_list[1], 1)
        elif dice_value == 3:
            self.assertEqual(freq_list[2], 1)
        elif dice_value == 4:
            self.assertEqual(freq_list[3], 1)
        elif dice_value == 5:
            self.assertEqual(freq_list[4], 1)
        elif dice_value == 6:
            self.assertEqual(freq_list[5], 1)


class TestGameClass(unittest.TestCase):
    """Test the Game Class."""

    def test_init_default_object(self):
        """Test Init Game."""
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
        """Player Rolls and Scores 1 Test."""
        game_test = game.Game()
        list_of_values = game_test.player_rolls(1)

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)

        self.assertTrue(list_of_values[4])

    def test_player_roll_dice_not_1(self):
        """Player Rolls and Score Not 1 Test."""
        game_test = game.Game()
        current_round_score_before = game_test.player_1.current_round_score
        list_of_values = game_test.player_rolls(4)

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertFalse(list_of_values[4])
        self.assertGreater(list_of_values[1], current_round_score_before)

    def test_player_holds(self):
        """Player Holds Test."""
        game_test = game.Game()
        num_rounds_before = game_test.player_1.num_rounds
        list_of_values = game_test.player_holds()
        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertIn(game_test.player_1.current_round_score, list_of_values)
        self.assertIn(game_test.player_1.num_rounds, list_of_values)

        self.assertGreater(list_of_values[3], num_rounds_before)

    def test_roll_and_hold(self):
        """Player Rolls and Holds Test."""
        game_test = game.Game()

        list_of_values = game_test.player_rolls(5)
        name_before = list_of_values[0]
        c_r_s_before = list_of_values[1]
        score_before = list_of_values[2]

        list_of_values_2 = game_test.player_holds()
        self.assertEqual(name_before, list_of_values_2[0])
        self.assertGreater(list_of_values_2[1], score_before)
        self.assertLess(list_of_values_2[2], c_r_s_before)

    def test_player_cheats(self):
        """Player Cheats Test."""
        game_test = game.Game()

        cheats_used_before = game_test.cheats_used
        num_rounds_before = game_test.player_1.num_rounds
        score_before = game_test.player_1.score

        list_of_values = game_test.player_cheats()
        score = list_of_values[0]
        cheats_used = list_of_values[3]
        num_rounds = list_of_values[2]

        self.assertTrue(cheats_used)
        self.assertNotEqual(cheats_used_before, cheats_used)
        self.assertGreater(num_rounds, num_rounds_before)
        self.assertGreater(score, score_before)

    def test_getting_scores(self):
        """Retrieving Player Info Test."""
        game_test = game.Game()

        list_of_values = game_test.get_player_info()

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertIn(game_test.player_1.num_rounds, list_of_values)
        self.assertIn(game_test.computer.difficulty, list_of_values)

    def test_scores_getting(self):
        """Retrieve Getting Scores."""
        game_test = game.Game()
        list_of_values = game_test.get_scores()

        self.assertIn(game_test.player_1.name, list_of_values)
        self.assertIn(game_test.player_1.score, list_of_values)
        self.assertIn(game_test.computer.name, list_of_values)
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


class TestHighScoreClass(unittest.TestCase):
    """Test the HighScore Class."""

    def test_init_default_object(self):
        """Test Init HighScore."""
        highscore_test = highscore.HighScore()
        self.assertIsInstance(highscore_test, highscore.HighScore)

    def test_write_file(self):
        """Testing file writing."""
        highscore_test = highscore.HighScore()
        highscore_test.set_info("nameEx", 55, 10, "medium")

        game_data = highscore_test.write_into_file("tryjson.json")

        expected_data = {
            "player_name": "nameEx",
            "score": 55,
            "num_rounds": 10,
            "difficulty": "medium"
        }

        self.assertEqual(game_data, expected_data)
        os.remove("tryjson.json")

    def test_write_to_already_exist_file(self):
        """Test writing into file that already has data."""
        highscore_test = highscore.HighScore()
        highscore_test.set_info("nameEx", 55, 10, "medium")
        highscore_test.write_into_file("tryjson.json")

        highscore_test = highscore.HighScore()
        highscore_test.set_info("nameEx2", 60, 11, "easy")
        game_data_2 = highscore_test.write_into_file("tryjson.json")

        expected_data = {
            "player_name": "nameEx2",
            "score": 60,
            "num_rounds": 11,
            "difficulty": "easy"
        }

        self.assertEqual(game_data_2, expected_data)
        os.remove("tryjson.json")

    def test_reading_scores_from_file(self):
        """Test Readinng From File."""
        highscore_test = highscore.HighScore()
        highscore_test.set_info("nameEx", 55, 10, "medium")
        with tempfile.NamedTemporaryFile(
            mode='w',
            delete=False,
            suffix=".json"
        ) as temp_file:
            temp_filename = temp_file.name
            game_data = {
                "player_name": "player_name",
                "score": "player_score",
                "num_rounds": "player_rounds",
                "difficulty": "player_difficulty"
                }
            json.dump([game_data], temp_file)

        try:
            scores = highscore_test.read_from_file(temp_filename)

            self.assertIsInstance(scores, list)

        finally:
            os.remove(temp_filename)

    def test_reading_scores_from_not_existing_file(self):
        """Test Reading From Non Existing File."""
        highscore_test = highscore.HighScore()
        highscore_test.set_info("nameEx", 55, 10, "medium")

        scores = highscore_test.read_from_file("non-existing.json")
        self.assertEqual(len(scores), 0)


class TestHistogramClass(unittest.TestCase):
    """Test the Histogram Class."""

    def test_init_default_object(self):
        """Test Init HighScore."""
        histogram_test = histogram.Histogram()
        self.assertIsInstance(histogram_test, histogram.Histogram)

    def test_write_file(self):
        """Testing file writing."""
        histogram_test = histogram.Histogram()
        name_example = "nameEx"
        freq_list_ex = []
        freq_list_ex.append(3)
        freq_list_ex.append(4)
        freq_list_ex.append(2)
        freq_list_ex.append(1)
        freq_list_ex.append(3)
        freq_list_ex.append(1)
        histogram_test.set_info(
            name_example,
            freq_list_ex)

        game_data = histogram_test.write_into_file("tryjson.json")

        expected_data = {
            "player_name": "nameEx",
            "hist": {
                "1": 3,
                "2": 4,
                "3": 2,
                "4": 1,
                "5": 3,
                "6": 1
                }
        }

        self.assertEqual(game_data, expected_data)
        os.remove("tryjson.json")

    def test_write_to_already_exist_file(self):
        """Test writing into file that already has data."""
        histogram_test = histogram.Histogram()
        name_example = "nameEx"
        freq_list_ex = [3, 4, 2, 1, 3, 1]
        histogram_test.set_info(
            name_example,
            freq_list_ex)

        histogram_test.write_into_file("tryjson.json")
        histogram_test = histogram.Histogram()
        histogram_test.set_info("nameEx2", [1, 2, 3, 4, 5, 6])
        game_data_2 = histogram_test.write_into_file("tryjson.json")

        expected_data = {
            "player_name": "nameEx2",
            "hist": {
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6
                }
        }

        self.assertEqual(game_data_2, expected_data)
        os.remove("tryjson.json")

    def test_reading_scores_from_file(self):
        """Test Readinng From File."""
        histogram_test = histogram.Histogram()
        name_example = "nameEx"
        freq_list_ex = [3, 4, 2, 1, 3, 1]
        histogram_test.set_info(
            name_example,
            freq_list_ex)
        with tempfile.NamedTemporaryFile(
            mode='w',
            delete=False,
            suffix=".json"
        ) as temp_file:
            temp_filename = temp_file.name
            game_data = {
                "player_name": "nameEx2",
                "hist": {
                    "1": 1,
                    "2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6
                    }
            }
            json.dump([game_data], temp_file)

        try:
            scores = histogram_test.read_histogram(temp_filename)

            self.assertIsInstance(scores, list)

        finally:
            os.remove(temp_filename)

    def test_reading_scores_from_not_existing_file(self):
        """Test Reading From Non Existing File."""
        histogram_test = histogram.Histogram()
        name_example = "nameEx"
        freq_list_ex = [3, 4, 2, 1, 3, 1]
        histogram_test.set_info(
            name_example,
            freq_list_ex)

        scores = histogram_test.read_histogram("non-existing.json")
        self.assertEqual(len(scores), 0)


if __name__ == "__main__":
    unittest.main()
