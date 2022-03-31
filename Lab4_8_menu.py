"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    8. Menu options
    Filename: menu.py
    Consider the following menu:

    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"

    Write a program that prints the menu to the screen and reads in the option
    selected by the user. For each option selected, add the selected string to
    the result and prompt the user again. If an invalid option is selected, your
    function should print Invalid option and present the menu again. Once
    0 -- Quit is selected, your function should print the resulting string that
    contains all of the options that were selected in the order they were selected
    For example:

    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 1
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 3
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 5
    Invalid option
    0 -- Quit
    1 -- Add "O"
    2 -- Add "oo"
    3 -- Add "xXx"
    Option: 0

    Result: OxXx
"""


def menu():
    # prints the menu to the screen
    print('0 -- Quit')
    print('1 -- Add "O"')
    print('2 -- Add "oo"')
    print('3 -- Add "xXx"')
    return 0


def main():
    menu()
    choice = input("Option: ")
    result = ''
    while choice != '0':
        if choice == '1':
            result = result + 'O'
            menu()
            choice = input('Option: ')
        elif choice == '2':
            result = result + 'oo'
            menu()
            choice = input('Option: ')
        elif choice == '3':
            result = result + 'xXx'
            menu()
            choice = input('Option: ')
        else:
            print('Invalid option')
            menu()
            choice = input("Option: ")
    print()
    print('Result:', result)


if __name__ == '__main__':
    main()
