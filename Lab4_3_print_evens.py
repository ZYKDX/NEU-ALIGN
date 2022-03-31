"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    3. Print evens
    Filename: print_evens.py
    Write a function called print_evens that prints the even numbers from 2 to 100 (inclusive)
"""


def print_evens():
    i = 2
    while i < 101:
        if i % 2 == 0:
            print(i)
        i += 1

