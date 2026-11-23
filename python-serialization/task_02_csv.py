#!/usr/bin/env python3
"""Convert a CSV file to a JSON file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Write the rows of csv_filename to data.json; True on success."""
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
        return True
    except (OSError, csv.Error):
        return False
