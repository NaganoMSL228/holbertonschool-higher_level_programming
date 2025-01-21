#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines
after each of these characters: ., ? and : .
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of ., ? and :.
    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text (str): The string of text to be formatted.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue
        result += char
        if char in ".?:":
            result += "\n\n"
            skip_space = True
        else:
            skip_space = False

    print(result.strip())
