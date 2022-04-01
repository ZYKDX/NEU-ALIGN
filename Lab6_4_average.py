"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    4. Calculate average
    Filename: average.py
    Write a function called calculate_average that receives a list of
    integer values and calculates the average of the values in the list.
    Your function should return 0 if there are no elements in the list.
"""


def calculate_average(my_list):
    if my_list == []:
        return 0
    else:
        total = 0
        for i in my_list:
            total += i
        return total / len(my_list)
