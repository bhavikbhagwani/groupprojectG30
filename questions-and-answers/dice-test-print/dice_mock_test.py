#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import unittest.mock
import dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    @unittest.mock.patch('builtins.print')
    def test_printing_last_roll(self, mock_print):
        """Check that the last roll is printed."""
        die = dice.Dice()

        res = die.roll()
        die.print_last_roll()

        # Get the arguments that the print function was called with
        args, _ = mock_print.call_args
        print(args)
        # Check if the last roll is printed
        self.assertTrue(str(res) in args[0], args)
        # Check if the value of rolls_made is printed
        self.assertTrue("1" in args[0], args)
