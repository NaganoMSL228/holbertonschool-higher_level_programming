#!/usr/bin/python3

"""Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str, optional): The name of the file to read. Defaults to "".
    """
with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
