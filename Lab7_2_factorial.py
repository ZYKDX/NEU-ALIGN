"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    2. Factorial
    Filename: factorial.py
    Write a recursive function called factorial that takes in a positive
    number (> 0) and returns its factorial.
    Recall that the factorial of n is n! = n * (n - 1) * ... 3 * 2 * 1.
"""


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)
