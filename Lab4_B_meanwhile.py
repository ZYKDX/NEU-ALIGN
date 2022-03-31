"""
    CS5001-5003 Spring 2022
    This program transfers strings to all-upper-case or all-lower-case
    Name: YUKUN ZHOU
"""


def print_lower(string):
    # receives a string and prints its lower-case version string
    str_length = len(string)
    index = 0
    while index < str_length:
        if ord(string[index]) >= 65 and ord(string[index]) <= 90:
            print(chr(ord(string[index]) + 32), sep = '', end = '')
        else:
            print(string[index], sep = '', end = '')
        index += 1
    return 0


def print_upper(string):
    # receives a string and prints its upper-case version string
    str_length = len(string)
    index = 0
    while index < str_length:
        if ord(string[index]) >= 97 and ord(string[index]) <= 122:
            print(chr(ord(string[index]) - 32), sep = '', end = '')
        else:
            print(string[index], sep = '', end = '')
        index += 1
    return 0


def main():
    # Test above functions on 3 examples each, including "Hello, world!"
    # example: print_lower("Hello, world!")
    string_1 = 'Hello, world!'
    print('The first string is:', string_1)
    print('print_lower result: ', end = '')
    print_lower(string_1)
    print('')
    print('print_upper result: ', end = '')
    print_upper(string_1)
    print('\n')
    
    string_2 = "Let's go, Rams!"
    print('The second string is:', string_2)
    print('print_lower result: ', end = '')
    print_lower(string_2)
    print('')
    print('print_upper result: ', end = '')
    print_upper(string_2)
    print('\n')
    
    string_3 = "This program is on NEU's Silicon Valley Campus"
    print('The third string is:', string_3)
    print('print_lower result: ', end = '')
    print_lower(string_3)
    print('')
    print('print_upper result: ', end = '')
    print_upper(string_3)
    print('\n')


if __name__ == '__main__':
    main()
