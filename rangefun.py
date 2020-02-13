a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
for num in range(a, b, c):
    print(num, end=' ')

# (a = 0, b = 4, c = 1) # output: 0 1 2 3
# (a = 0, b = -4, c = -1) # output: -3 -2 -1 0
# (a = 0, b = 11, c = 2) # output: 10 8 6 4 2
# (a = 1, b = 48, c = 46) # output: 1 47
