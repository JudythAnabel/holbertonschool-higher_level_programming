#!/usr/bin/env python3
"""Serialize a dictionary to XML and deserialize it back."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save dictionary to filename as XML under a <data> root."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Return a dictionary built from the XML in filename."""
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
