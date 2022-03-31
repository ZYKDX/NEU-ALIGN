"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    5. tuple to list
    Filename: convert_tuple.py
    Write a function called convert_tuple that takes a tuple as a parameter and
    returns a list that contains all of the same elements in the same order
"""


def convert_tuple(tup):
    # takes a tuple
    # returns a list that contains all the elements, same order
    new_ls = []
    i = 0
    while i < len(tup):
        new_ls.append(tup[i])
        i += 1
    return new_ls
