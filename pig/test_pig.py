

"""Unit testing."""

import unittest
import dice

class TestDiceClass(unittest.TestCase):  # noqa: H601
    """Test the class."""


    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()