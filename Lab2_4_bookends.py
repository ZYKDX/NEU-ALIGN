"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    4. Numeric Bookends
    Filename: bookends.py
    Write a program that reads a 4-digit number
    from the keyboard and prints the first and
    last digits of the number. For example,
    Enter number: 1234
    The first number is 1
    The last number is 4
"""


def main():
    number = int(input("Enter number: "))
    
    first_digit = number // 1000
    last_digit = number % 10

    print("The first number is", first_digit)
    print("The last number is", last_digit)


if __name__ == '__main__':
    main()
