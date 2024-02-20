#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_a_dice(self):
        """Rool a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= die.faces
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
