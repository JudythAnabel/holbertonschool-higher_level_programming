#!/usr/bin/env python3
"""Serialize a dictionary to a JSON file and load it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Save data to filename as JSON, replacing the file if it exists."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Return the Python dictionary stored as JSON in filename."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
