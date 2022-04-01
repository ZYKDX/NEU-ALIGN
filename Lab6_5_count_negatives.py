"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    5. Count negatives
    Filename: count_negatives.py
    Write a function called count_negatives that receives a list of
    integer values and returns how many of the values in the list are negative.
    Your function should return 0 if there are no elements in the list.
"""


def count_negatives(my_list):
    if my_list == []:
        return 0
    count = 0
    for i in my_list:
        if i < 0:
            count += 1
    return count
