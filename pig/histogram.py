"""
Histogram class.

This class instantiates a Histogram
and contains some methods to read and write scores into/from file
"""

import json


class Histogram:
    """Example of Histogram class."""

    def __init__(self):
        """Init HighScore."""
        self.name = None
        self.frequency_list = None

    def set_info(self, name, freq_list):
        """Set info to write into file."""
        self.name = name
        self.frequency_list = freq_list

    def write_into_file(self, filename):
        """Write dice frequency of this player."""
        histogram_array = self.frequency_list
        histogram_map = {
            str(i+1): freq for i,
            freq in enumerate(histogram_array)
            }
        histogram_data = {
            "player_name": self.name,
            "hist": histogram_map
            }

        try:
            with open(filename, "r", encoding="utf-8") as file:
                ex_data = json.load(file)
        except FileNotFoundError:
            ex_data = []

        ex_data.append(histogram_data)

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as histogram_json_file:
            json.dump(ex_data, histogram_json_file, indent=2)

        return histogram_data

    def read_histogram(self, filename):
        """Read histogram frequency from File."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                histogram_data = json.load(file)
        except FileNotFoundError:
            histogram_data = []

        return histogram_data
