"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    7. Both sides
    Filename: both_sides.py
    Write a program that prompts with "Enter value: " and reads in an
    integer value from the keyboard and prints the appropriate message
    depending upon the value of that input according to the following table:
    Even or odd    Value      Message
    Even           negative   "even negative number"
    Even(and 0)    positive   "even positive number"
    Odd            negative   "odd negative number"
    Odd            positive   "odd positive number"

    Hint: recall that numbers are even if they divide evenly by 0
"""


def main():
    number = int(input('Enter value: '))
    if number < 0 and number % 2 == 0:
        print('even negative number')
    elif number >= 0 and number % 2 == 0:
        print('even positive number')
    elif number < 0 and number % 2 == 1:
        print('odd negative number')
    else:
        print('odd positive number')


if __name__ == '__main__':
    main()
    
