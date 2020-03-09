# # The Julian date of a year is the ordinal number of any date within the year.  For example, January 1 is always
# # Julian date 1, February 1 is Julian date 32, and December 31 is Julian date 365 in non-leap years and 366 in leap
# # years.
# #
# # Here's a way of calculating the Julian date daynum. Use int arithmetic in these calculations:
# #
# # (1) daynum = 31*(month−1) + day
# # (2) If the month is after February, subtract (4*month + 23) // 10 from daynum
# # (3) If it’s a leap year and after February 29, add 1 to daynum
# #
# # Using this algorithm, write a function julian(day,month,year) which returns the int Julian date of its arguments.
# # Define a main() function which reads the date from the user as three separate int values; you don't have to verify
# # that it's valid.  Then call your function passing the three input arguments and print the returned int result.


def julian(day, month, year):
    if month == 1:
        daynum = 31 * (month - 1) + day

    if month > 2:
        daynum = - (4 * month + 23) // 10

    if (year % 4 == 0 or year % 400 == 0) and (month >= 2 and day > 29):
        print("It's leap year")
        daynum = - (4 * month + 23) // 10 + 1

    return daynum


def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the  month: "))
    day = int(input("Enter the day: "))

    print(day, "/", month, "/", year, "is", julian(day, month, year), "Julian days")


main()
