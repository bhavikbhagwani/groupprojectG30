#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import logging
import unittest
import sys
import dice


class TestDiceWithLogClass(unittest.TestCase):
    """Test the class."""

    def test_roll_a_dice(self):
        """Roll a dice and check value is in bounds."""
        die = dice.Dice()

        res = die.roll()
        exp = 1 <= res <= die.faces
        self.assertTrue(exp)

        # Print messages using logging
        logging.basicConfig(stream=sys.stderr)
        log = logging.getLogger("LOG")
        log.warning(f"Dice was: {res}")
