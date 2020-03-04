

def f2c(fahr):

    Celsius = (fahr - 32) * 5 / 9
    # Fahrenheit = 9.0/5.0 * Celsius + 32
    rounded_Celsius = round(Celsius, 2)
    result = rounded_Celsius
    return result


def main():
    value = float(input("Enter the  temperature in degree F: "))
    print(value,"degree F is",f2c(value),"degree C")


# main()

