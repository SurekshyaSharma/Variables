# Write a Python program that reads the taxable income income as a float value from the user, then calculates and
# prints out the highest percentage tax rate for an unmarried individual with that taxable income. Use the table to
# the right. For example, if an income of 47000 is entered, then your program should print 22%, since 84200 >= 47000>
# 39475 and the table indicates that incomes in this range have this tax rate.  You should also check that the
# entered income is >= 0.0; otherwise print "Bad input" and quit.
user_income = float(input("Enter your Income: "))
# 10% = 0 12%= 9700, 22 = 39475, 24= 84200,32= 160725, 35=204100,37=510300

if user_income <= 0:
    print("Bad Input")
    user_income = float(input("Enter your Income: "))
    if user_income >= 510300:
        print("Your tax percentage is 37%")
    elif 204100 <= user_income < 510300:
        print("Your tax percentage is 35 %")
    elif 160725 <= user_income < 204100:
        print("Your tax percentage is 32 %")
    elif 84200 <= user_income < 160725:
        print("Your tax percentage is 24 %")
    elif 39475 <= user_income < 84200:
        print("Your tax percentage is 22 %")
    elif 9700 <= user_income < 39475:
        print("Your tax percentage is 12 %")
    elif 0 <= user_income < 9700:
        print("Your tax percentage is 10 %")
else:
    if user_income >= 510300:
        print("Your tax percentage is 37%")
    elif 204100 <= user_income < 510300:
        print("Your tax percentage is 35 %")
    elif 160725 <= user_income < 204100:
        print("Your tax percentage is 32 %")
    elif 84200 <= user_income < 160725:
        print("Your tax percentage is 24 %")
    elif 39475 <= user_income < 84200:
        print("Your tax percentage is 22 %")
    elif 9700 <= user_income < 39475:
        print("Your tax percentage is 12 %")
    elif 0 <= user_income < 9700:
        print("Your tax percentage is 10 %")
