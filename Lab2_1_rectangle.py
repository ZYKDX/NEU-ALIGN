"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    1. Rectangle
    Filename: rectangle.py
    Write a program that reads the length of a rectangle's sides and then prints
        the area and perimeter of the rectangle
        the length of the diagonal (use the Pythagorean theorem)
    Hint: you can calculate the square root of a number by raising it to the 0.5 power. For example:
    Enter width: 9
    Enter height: 3
    The area of the rectangle is 27.0
    The perimeter of the rectangle is 24.0
    The diagonal is 9.486832980505138
"""


def main():

    # reads the length of a rectangle's sides
    # print area, perimeter, length of diagonal of the rectangle

    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    area = width * height
    perimeter = 2 * width + 2 * height
    diagonal = (width * width + height * height) ** 0.5

    print("The area of the rectangle is", area)
    print("The perimeter of the rectangle is", perimeter)
    print("The diagonal is", diagonal)


if __name__ == '__main__':
    main()
