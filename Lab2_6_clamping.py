"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    6. Clamping
    Filename: clamping.py
    Write a program that reads in a number from the keyboard.
    Your program should ensure that the value entered is between
    1 and 100 by clamping it and then print it to the screen.
    Clamping a number means that any value less than the lowest value
    is set to the lowest value and that any value larger than the
    largest value is set to the largest value.
    Examples:
    
    Enter value: 103
    Too big, clamping required
    Value is 100

    Enter value: -12
    Too small, clamping required
    Value is 1

    Enter value: 42
    Value is 42
"""


def main():
    number = int(input("Enter value: "))
    if number < 1:
        print("Too small, clamping required")
        print("Value is 1")
    elif number > 100:
        print("Too big, clamping required")
        print("Value is 100")
    else:
        print("Value is", number)


if __name__ == '__main__':
    main()
