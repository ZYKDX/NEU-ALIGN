"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    4. Lower triangle
    Filename: lower_triangle.py
    Write a recursive function called lower_triangle that takes in a number greater
    than or equal to 3 and prints an lower left triangle of that size. For example
    lower_triangle(5) prints

    *
    **
    ***
    ****
    *****
    You can assume that the input is greater than or equal to 3
"""


def lower_triangle(n):
    if n == 3:
        print("*\n**\n***")
    else:
        lower_triangle(n - 1)
        print("*" * n)
