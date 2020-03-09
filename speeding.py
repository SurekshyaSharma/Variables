# The speeding ticket fine policy in Beldenville is $50 plus $5 for each mph over the limit, plus a penalty of $200
# for any speed over 90 mph. Assume that the limit is less than 90 mph. Write a program that reads a float speed
# limit and another float as the measured speed, then either prints a message indicating the speed was legal or
# prints the amount of the fine if the speed was illegal.


def speeding_fine(speed_limit, measured_speed):

    if speed_limit > 90:
        over_limit = speed_limit - measured_speed
        fine = 50 + 5 * over_limit
        fine = fine + 200
        return fine
        return True


def main():
    speed_limit = float(input("Enter the speed: "))
    measured_speed = float(input("Enter the measured speed: "))

    if speeding_fine(speed_limit,measured_speed):
        print("The speed was illegal.","Your fine is",speeding_fine(speed_limit, measured_speed))
    else:
        print("You are within the driving speed limit.")

main()
