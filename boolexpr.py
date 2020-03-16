# Write a Boolean (bool) function is_in_semester(month,day)that returns True when month/day falls within the dates of
# our current GPS Spring Semester 2020, starting on February 3 and ending on May 22. If month/day falls outside this
# range (which includes both starting and ending dates), return False . Then write a main() function that reads
# integers month and day from the user, calls is_in_semester(month,day) , then prints out 'month/day is in Spring
# Semester' or 'month/day is NOT in Spring Semester' . Example for month==4 , day==7 => print ' 4/7 is in Spring
# Semester' . Finally, call main() as the last statement in your .py file. Note that your function should only return
# True or False , with main() calling is_in_semester(...) , then printing out the text which depends upon its bool
# returned value. No "chatterbox functions"!


def is_in_spring(month, day):  # between 02/3 and 5/22, inclusive

        if month>=2 and month<=5:
            if month ==2 and day>=3:
                return True
            elif month==3 and day>=1 and day<32:
                return True
            elif month ==4 and day>=1 and day<32:
                return True
            elif month==5 and day>=1 and day<=22:
                return True
        else:
            return False


def main():
    month = int(input("Enter month number: "))
    day = int(input("Enter day number: "))

    # your solution follows...
    if is_in_spring(month, day):
        print(month, "/", day, "is in spring 2020")
    else:
        print(month, "/", day, "is not spring 2020")


main()
