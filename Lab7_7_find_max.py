"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    7. Find max
    Filename: find_max.py
    Write a recursive function called find_max that takes in a list of integers
    and returns the maximum value from that list.
    Use an index to keep track of the current element by writing a helper function
    that finds the maximum of a list of integers starting at the element at the
    current index
"""


# use an index to keep track of the current element
# by writing a helper function that finds the max start at the current index
def helper(my_list, my_index):
    temp = my_list[my_index]
    for i in my_list[my_index:]:
        if i > temp:
            temp = i
    return temp


def find_max(my_list):
    # list of int
    # max value in the list
    count = len(my_list)
    if count == 0:
        return 0.1
    elif count == 1:
        return my_list[0]
    elif my_list[0] > helper(my_list, 1):
        return my_list[0]
    else:
        return helper(my_list, 1)
