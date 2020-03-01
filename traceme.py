#
# H3-5: run the following in the PyCharm debugger and print
#       the following requested info...

import math

# What are we trying to accumulate in val, when the following code is executed?
# Hint: it doesn't do it correctly... Why?

num = int(input("enter number of floats: "))

val = 0.0

for b in range(num):
    a = float(input("enter next float: "))
    val = min(val, abs(a - math.pi))

    print("set breakpoint on this line...")  # LOCATION 1
    # values 5, 3.0, 3.1, 3.14, 3.13, 3.141

    # a = 3.0, b = 1, num = 5, val = 0.0
    # a = 3.1, b = 1, num = 5, val = 0.0
    # a = 3.14, b = 2, num = 5, val = 0.0
    # a = 3.13, b = 3, num = 5, val = 0.0
    # a = 3.141, b = 4, num = 5, val = 0.0
print(val)

print("set another breakpoint on this line...")  # LOCATION 2:

# a = 3.0, b = 0, num = 5, val = 0.0
# a = 3.1, b = 1, num = 5, val = 0.0
# a = 3.14, b = 2, num = 5, val = 0.0
# a = 3.13, b = 3, num = 5, val = 0.0
# a = 3.141, b = 4, num = 5, val = 0.0

# list values of a, b, and val at LOCATION 1
#    for each time through loop (b=0,1,2,3,4),

# then list final values of a, b, and val at LOCATION 2
