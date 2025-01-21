#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The 5-text_indentation module supplies one function, text_indentation(text).
For example,

>>> text_indentation("Hello. My name is Joe. What is your name?")
Hello.
My name is Joe.
What is your name?
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text isn't a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]))
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
