"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    6. To squares
    Filename: to_squares.py
    Write a recursive function called to_squares that takes in a list of integers
    and an index of the one element in the list and returns the same list where the
    elements from the provided index to the end of the list have been squared
"""


def to_squares(my_list, my_index):
    if my_list == []:
        return my_list
    if my_index == len(my_list) - 1 or my_index == -1:
        my_list[my_index] = my_list[my_index] ** 2
        return my_list
    else:
        temp = my_list[my_index] ** 2
        my_list = to_squares(my_list, my_index + 1)
        my_list[my_index] = temp
        return my_list
