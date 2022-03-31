"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    9. Building a string
    Filename: build_string.py
    Write a function called build_string that takes a string value, and three
    integer values and returns a single string containing 3 lines. One each line,
    the string value is repeated the specified number of times. For example, if I
    were to call it with build_string("hi", 4,2,3) I would get the string

    hihihihi
    hihi
    hihihi
"""


def build_string(string, num1, num2, num3):
    return string * num1 + '\n' + string * num2 + '\n' + string * num3 
