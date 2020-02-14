# inputs from the user
start = int(input("Enter the first number:"))
stop = int(input("Enter the second number:"))
# loop for
product = 0
for i in range(start, stop+1):
    product = product + (i ** 2)
print(product)
