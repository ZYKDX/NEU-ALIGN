"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    7. Calculations
    Filename: calculations.py
    Write a program that asks the user for a positive integer representing the number
    of integer values to read (Enter the number of values to read:) The program should
    then read the specified number of integer values from the keyboard and then it
    should print the sum (The sum is) and the average (The average is) of the numbers
    that were entered on seperate lines
"""


def calculations():
    input_count = int(input('Enter the number of values to read: '))
    if input_count <= 0:
        print('The sum is 0')
        print('The average is 0')
        return 0
    else:
        i = 0
        total = 0
        while i < input_count:
            current_value = int(input('Enter an integer: '))
            total += current_value
        print('The sum is', total)
        print('The average is', total / input_count)
        return 0


def main():
    calculations()


if __name__ == '__main__':
    main()
