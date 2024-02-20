#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import main


class TestSomeClass(unittest.TestCase):
    """Test the class."""

    def test_highscore1(self):
        """Verify that a specific exception is raised in the code."""
        obj = main.SomeClass()

        with self.assertRaises(FileNotFoundError):
            obj.highscore1()

    def test_highscore2_but_fail(self):
        """We can not verify wether exception was raised or not.

        The method catches the exception itself.
        """
        obj = main.SomeClass()
        obj.highscore2()

        # This can never be verified
        # with self.assertRaises(FileNotFoundError):
        #     obj.highscore2()
