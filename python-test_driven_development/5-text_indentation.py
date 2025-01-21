#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines
after each of the characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.
    There should be no extra spaces at the start or end of lines.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i, length = 0, len(text)
    result = ""

    while i < length:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip all spaces after punctuation
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result.strip(), end="")
