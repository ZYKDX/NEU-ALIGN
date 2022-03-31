"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    4. List to string
    Filename: list_to_string.py
    Write a function called list_to_string that takes a list as a parameter
    and returns a string with each element of the list on its own line. For
    example

    khoury
    college
    align
    masters
"""


def list_to_string(ls):
    # takes a list
    # returns a string, with each element of the list on its own line
    if len(ls) == 0:
        return ''
    elif len(ls) == 1:
        return ls[0]
    new_str = ''
    i = 0
    while i < len(ls) - 1:
        new_str = new_str + str(ls[i]) + '\n'
        i += 1
    new_str = new_str + str(ls[-1])
    return new_str
