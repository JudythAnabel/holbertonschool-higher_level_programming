#!/usr/bin/env python3
"""Serialize and deserialize a custom object with pickle."""
import pickle


class CustomObject:
    """A simple object with a name, an age and a student flag."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Save this object to filename with pickle; None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from filename; None on failure."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, EOFError, pickle.UnpicklingError,
                AttributeError, ImportError, IndexError, ValueError):
            return None
