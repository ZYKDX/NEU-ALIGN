"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    6. Area of Triangle
    Filename: area_triangle.py
    Write a function called area_triangle that returns the area of a triangle
    given the length of its three sides as parameters.
    Heron's formula
    math.sqrt()
"""


import math


def area_triangle(len1, len2, len3):
    s = (len1 + len2 + len3) / 2
    area = math.sqrt(s * (s - len1) * (s - len2) * (s - len3))
    return area
