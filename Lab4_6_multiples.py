"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    6. Multiples
    Filename: multiples.py
    Write a program that asks the user for a non_zero value and then prompts the
    user to enter multiples of that number. It should ensure that the number is
    a multiple of the integer value and asks the user to Try again: until a multiple
    is entered. For example, if 5 is entered as the integer then

    Enter a non-zero integer: 5
    Enter multiple: 26
    Try again: 67
    Try again: 93
    Try again: 40
"""


def main():
    base = int(input('Enter a non-zero integer: '))
    multiple = int(input('Enter multiple: '))
    while multiple % base != 0:
        multiple = int(input('Try again: '))


if __name__ == '__main__':
    main()
