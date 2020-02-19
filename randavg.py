import random

numRolls = int(input("Enter the number:"))
total_sum = 0
number = 0
for num in range(numRolls):

    number = random.randint(1,6)
    total_sum = total_sum + number
    print(number)
    print("------------------")

print("The total sum is ", total_sum)

average_Roll_Value = (total_sum / numRolls)
print("The average roll value is :", average_Roll_Value )

