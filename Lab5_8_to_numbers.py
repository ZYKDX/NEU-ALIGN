"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    8. Convert to numbers
    Filename: to_numbers.py
    Write a function called to_numbers that receives a list of string values
    each of which represents a number and returns a list of floats.
"""


def to_numbers(ls):
    # takes a list of string values
    # transfer the values to float and return
    new_ls = ls
    i = 0
    while i < len(ls):
        new_ls[i] = float(ls[i])
        i += 1
    return new_ls
