"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    5. Sum values
    Filename: sum_values.py
    Write a recursive function called sum_values that takes in a list of integers
    and an index of one element in the list and returns the sum of all values/elements
    in the list starting with the element with the provided index and ending with the
    last element in the list
"""


def sum_values(my_list, my_index):
    if my_list == []:
        return 0
    if my_index == len(my_list) - 1 or my_index == -1:
        return my_list[my_index]
    else:
        return sum_values(my_list, my_index + 1) + my_list[my_index]
