#!/usr/bin/python3


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text to be formatted

    Raises:
    TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue
        
        result += char
        
        if char in punctuation:
            result += '\n\n'
            skip_space = True
        else:
            skip_space = False

    print(result.strip())
