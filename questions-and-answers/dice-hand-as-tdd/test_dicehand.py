#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dicehand


class TestDiceHandClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        hand = dicehand.DiceHand()
        self.assertIsInstance(hand, dicehand.DiceHand)

    def test_roll_five_dices(self):
        """Roll five dices."""
        hand = dicehand.DiceHand()
        self.assertIsInstance(hand, dicehand.DiceHand)

        hand.addDices(5)
        res = hand.roll()
        for die in res:
            exp = 1 <= die.get_last_roll() <= die.faces
            self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
