"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    6. Read values
    Filename: read_values.py
    Write a function called read_values that returns a list of positive integer
    values that are read from the keyboard one at a time. The values should appear
    in the list in the order that they were entered. Any non-positive integer values
    should stop adding elements to the list
    For example:

    Enter a number: 77
    Enter a number: 975
    Enter a number: 234
    Enter a number: -1
    [77, 975, 234]

    Remember, because your program includes reading from the keyboard,
    it should include a conditional main method.
"""


def read_values():
    # read positive values from the keyboard
    # stops when non-positive value is entered
    # returns a list of the entered values, ordered
    new_ls = []
    temp_num = int(input('Enter a number: '))
    while temp_num > 0:
        new_ls.append(temp_num)
        temp_num = int(input('Enter a number: '))
    return new_ls
