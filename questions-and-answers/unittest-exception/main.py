#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main for testing code samples."""

import random


class SomeClass():
    """Example of a class."""

    file = "highscore.json"

    def highscore1(self):
        """Open the highscore file."""
        with open(self.file, "r") as highscore:
            print("The file {} is now opened.".format(self.file))

    def highscore2(self):
        """Open the highscore file."""
        try:
            with open(self.file, "r") as highscore:
                print("The file {} is now opened.".format(self.file))
        except FileNotFoundError:
            print("Exception raised: File Not Found")


def main():
    """Use the class."""
    object = SomeClass()

    print("Try highscore1")
    try:
        object.highscore1()
    except FileNotFoundError:
        print("Exception raised: File Not Found")

    print("Try highscore2")
    object.highscore2()


if __name__ == '__main__':
    main()
