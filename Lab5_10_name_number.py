"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    10. Name Number
    Filename: name_number.py
    Numerologists claim to be able to determine a person's character
    traits based on the "numeric value" of a name. The value of a name
    is determined by summing up the values of the letters of the name
    where "a" is 1, "b" is 2, "c" is 3, etc., up to "z" being 26.
    For example, the name "Jump" would have the value 10 + 21 + 13 + 16 = 60
    (which happens to be a very auspicious number, by the way) ...
    Write a function called name_number that returns the numeric value
    of a single named provided to it.
"""


def name_number(name):
    # takes a string
    # transfer each letter to a value, a=1, b=2, ...
    # get the total value for the name, and return
    name_num_val = 0
    i = 0
    while i < len(name):
        if ord(name[i]) >= ord('a') and ord(name[i]) <= ord('z'):
            name_num_val += ord(name[i]) - ord('a') + 1
        elif ord(name[i]) >= ord('A') and ord(name[i]) <= ord('Z'):
            name_num_val += ord(name[i]) - ord('A') + 1
        i += 1
    return name_num_val
