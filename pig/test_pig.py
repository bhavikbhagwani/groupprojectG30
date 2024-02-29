

"""Unit testing."""

import unittest
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

    

class TestComputerClass(unittest.TestCase):
    """Test the Computer Class."""

    def test_roll_a_dice_for_computer(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()

        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

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
        
if __name__ == "__main__":
    unittest.main()
