"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    1. Print multiples of 5
    Filename: multiples.py
    Write a program that reads in a positive integer value from
    the keyboard and uses a for loop to print the multiples of 5
    that are less than or equal to the number that was entered.
    For example,

    Enter a positive integer: 42
    5
    10
    15
    20
    25
    30
    35
    40
"""


def main():
    num = int(input("Enter a positive integer: "))
    if num < 5:
        return -1
    else:
        for i in range(num // 5):
            print(5 * (i + 1))


if __name__ == '__main__':
    main()
