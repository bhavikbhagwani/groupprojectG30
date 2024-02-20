#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for testing code samples."""

import random


class SomeClass():
    """Example of a class."""

    def randomize_number(self):
        """Generate a new number."""
        self.magic_number = random.randint(1, 100)

    def check_number(self):
        """Check the number is valid."""
        if self.magic_number == None:
            raise Exception("You forgot to init the game.")
        elif self.magic_number == 13:
            raise ValueError("The game stopped due to unlucky numbers.")

        # All is fine, do some stuff

def main():
    """Use the class."""
    obj = SomeClass()

    print("randomize_number")
    obj.randomize_number()

    print("check_number")
    obj.check_number()


if __name__ == '__main__':
    main()
