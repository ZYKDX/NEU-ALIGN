"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    1. Count up
    Filename: count_up.py
    Write a function called count_up that takes a positive integer as a parameter
    and then prints all of the numbers between 1 and that integer (both inclusive)
"""


def count_up(parameter):
    # takes a positive int and prints from 1 to parameter
    i = 1
    while i <= parameter:
        print(i)
        i += 1

