"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    2. Add spaces
    Filename: add_spaces.py
    Write a function called add_spaces that takes a string as input and
    uses a loop to append each character of the string on the same line
    with 3 spaces between each letter. For example, the call
    add_spaces("Computer") would return this string:

    C   o   m   p   u   t   e   r
"""


def add_spaces(string):
    # takes a string
    # append each character with 3 spaces
    # return a single line of string
    if len(string) <= 1:
        return string
    new_str = ''
    i = 0
    while i < len(string) - 1:
        new_str = new_str + string[i] + '   '
        i += 1
    new_str = new_str + string[-1]
    return new_str
