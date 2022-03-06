# Name: Yukun Zhou
# Date: 02/13/2022
# This function receives a year integer and tells if it's leap year
# Returns True if it is leap year and False if not


def is_leap_year(year):
    # this function returns True if the year is leap and False if not

    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def main():
    user_test = input("To enter the test year manually, press 1; for  preset cases, press 2: ")
    if user_test == '1':
        for i in range(0,6):
            year = int(input("Please enter a year greater than 0: "))
            if is_leap_year(year) == True:
                print("The year", year, "is a leap year.")
            else:
                print("The year", year, "is not a leap year")
    else:
        year = 2000
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        year = 2001
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        year = 2002
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        year = 2003
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        year = 2004
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        year = 2100
        if is_leap_year(year) == True:
            print("The year", year, "is a leap year.")
        else:
            print("The year", year, "is not a leap year")
        
if __name__ == '__main__':
    main()
