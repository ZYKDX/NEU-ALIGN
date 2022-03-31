"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    3. Length
    Filename: length.py
    Write a program that reads a measurement in
    meters and the converts it to inches, feet,
    and miles. There are 39.3701 inches in a meter. For example:
    Enter length: 42
    The length in inches is 1653.5442
    The length in feet is 137.79528
    The length in miles is 0.026097582
"""


def main():
    meter = float(input("Enter length: "))
    inch = meter * 39.3701
    feet = inch / 12
    mile = feet / 5280
    print("The length in inches is", inch)
    print("The length in feet is", feet)
    print("The length in miles is", mile)


if __name__ == '__main__':
    main()
