"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    2. Count down
    Filename: count_down.py
    Write a function called count_down that takes a positive integer as a parameter
    and then prints all of the numbers starting with the integer down to 1 (both inclusive)
"""


def count_down(parameter):
    while parameter >= 1:
        print(parameter)
        parameter -= 1

