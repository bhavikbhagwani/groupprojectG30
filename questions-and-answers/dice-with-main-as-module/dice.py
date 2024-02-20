#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a module rolling dices."""

# pylint: disable=W0603

import random

FACES = 6
ROLLS_MADE = 0


def init():
    """Roll a dice once and return the value."""
    global ROLLS_MADE

    random.seed()
    ROLLS_MADE = 0


def roll():
    """Roll a dice once and return the value."""
    global ROLLS_MADE

    ROLLS_MADE += 1
    return random.randint(1, FACES)


def get_rolls_made():
    """Get number of rolls made."""
    return ROLLS_MADE
