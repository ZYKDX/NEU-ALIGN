"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    3. Upper triangle
    Filename: upper_triangle.py
    Write a recursive function called upper_triangle that takes in a number greater
    than or equal to 3 and prints an upper left triangle of that size. For example
    upper_triangle(5) prints

    *****
    ****
    ***
    **
    *
    You can assume that the input is greater than or equal to 3
"""


def upper_triangle(n):
    # n >= 3
    if n == 3:
        print("***\n**\n*")
    else:
        print("*" * n)
        upper_triangle(n - 1)
