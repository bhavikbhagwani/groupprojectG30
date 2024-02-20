#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import io
import unittest
import sys
import dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    def test_printing_last_roll(self):
        """Check that the last roll is printed."""
        die = dice.Dice()

        res = die.roll()

        # Prepare to capture the output
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        # Call the method(s) printing to stdout (and capture the output)
        die.print_last_roll()

        # Reset the capture
        sys.stdout = sys.__stdout__

        # get the captured output
        output = capturedOutput.getvalue()

        # Check if the last roll is printed
        self.assertTrue(str(res) in output)
        # Check if the value of rolls_made is printed
        self.assertTrue("1" in output)
