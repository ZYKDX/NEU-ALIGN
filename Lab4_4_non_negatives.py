"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    4. Non-negatives
    Filename: non_negatives.py
    Write a program that prompts the user with Enter an integer: and reads integer
    values in from the keyboard. When a non-negative value is read, it should print
    the value to the screen. When a negative value is read, it should stop.
"""


def main():
    number = int(input('Enter an integer: '))
    while number >= 0:
        print(number)
        number = int(input('Enter another integer: '))
    return -1


if __name__ == '__main__':
    main()
