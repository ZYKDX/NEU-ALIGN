"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    4. First
    Filename: first.py
    Write a function called first that receives two parameter values and returns the
    one that comes first. In the case of two numeric values, it would return the smaller
    of the two. In the case of two strings, it would return the one that comes first
    lexicographically (e.g. first("cat", "dog") returns "cat")
"""


def first(parameter_one, parameter_two):
    if parameter_one < parameter_two:
        return parameter_one
    return parameter_two
