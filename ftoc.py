def f2c(fahr):
    Celsius = (fahr - 32) * 5 / 9
    # Fahrenheit = 9.0/5.0 * Celsius + 32
    Celsius = str(round(Celsius, 2))
    fahr = str(fahr)
    print(Celsius)
    print(fahr + " degree F is " + Celsius + " degree C.")


def main():
    value = float(input("Enter the  temperature in degree F: "))
    f2c(value)


main()
