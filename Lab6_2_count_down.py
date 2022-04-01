"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    2. Count down
    Filename: count_down.py
    Write a function called count_down that uses a for loop to print the count
    down from 100 to 0 (inclusive) by 5s. Instead of printing 0, your code should
    print Blastoff!
"""


def count_down():
    for i in range(100, 0, -5):
        print(i)
    print("Blastoff!")
