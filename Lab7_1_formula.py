"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    1. Formula
    Filename: formula.py
    Write a function called formula that returns the result of the
    following mathematical formula. You should write your solution recursively.
    Assume x is a positive integer.

    f(x) = 3 if x=1;
    f(x) = 2f(x-1)+5 otherwise
"""


def formula(x):
    if x == 1:
        return 3
    return 2 * formula(x - 1) + 5
