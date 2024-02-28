

"""Unit testing."""

import unittest
import dice
import computer


class TestDiceClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_roll_a_dice_for_computer(self):
        """Roll a dice and check value is in bounds."""
        computer_test = computer.Computer()

        res = computer_test.return_computer_rolled_dice_value()
        exp = 1 <= res <= 6
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
