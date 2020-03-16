
# The year y is a leap year if and only if y is evenly divisible by 4 but not by 100, OR if y is evenly divisible by
# 400.  Thus, 2020 is a leap year (evenly divisible by 4 but not by 100.  1900 is NOT a leap year, since it's evenly
# divisible by 100 but NOT by 400.  And 2000 IS a leap year, since it's evenly divisible by 400.

# Python program to check if year is a leap year or not


def is_leap(year):
    if year % 4 == 0 or year % 400 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


def test_Two_Thousand():
    assert True == is_leap(2000)


def test_Nineteen_hundred():
    assert False == is_leap(1900)


def test_Two_Thousand_two():
    assert False == is_leap(2002)


def test_Twenty_Sixteen():
    assert True == is_leap(2016)


def test_Two_Thousand():
    assert True == is_leap(2024)


def test_Two_Thousand_Four():
    assert True == is_leap(2004)


def test_2040():
    assert True == is_leap(2040)


def test_2039():
    assert False == is_leap(2039)


def test_2033():
    assert True == is_leap(2032)


def test_2012():
    assert True == is_leap(2012)


def test_2032():
    assert True == is_leap(2012)

