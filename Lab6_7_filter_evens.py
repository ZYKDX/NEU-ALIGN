"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    7. Filter evens
    Filename: filter_evens.py
    Write a function called filter_evens that receives a list of
    integer values and returns a new list that contains only the
    even elements of the argument.
"""


def filter_evens(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
