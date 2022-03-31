"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    7. Square each
    Filename: square_each.py
    Write a function called square_each that receives a list as a parameter
    and returns the same list that has been modified so that all the elements
    are squared
"""


def square_each(ls):
    # takes a list
    # square all the elements, and return
    new_ls = ls
    i = 0
    while i < len(ls): 
        new_ls[i] = ls[i] * ls[i]
        i += 1
    return new_ls
