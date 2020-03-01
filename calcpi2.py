# def myPi(n):
#     denominator = 1
#     addto = 1
#
#     for i in range(n):
#         denominator = denominator + 2
#         addto = addto - (1/denominator)
#         denominator = denominator + 2
#         addto = addto + (1/denominator)
#
#     pi = addto * 4
#
#     return(pi)
#
# print(myPi(1000000))

# Hint: use a loop with header for count in range(num_terms),
# after you initialize a float accumulator pi_estimate to 0.0 and sign to 1.0.
# Your indented loop body should first calculate term = sign / (2*count + 1),
# then add term to your pi_estimate accumulator.
# The final statement within your loop body should be sign = -sign
# so that the term calculated in the next iteration of the for-loop will have the opposite sign.
# After the loop ends, calculate and print 4*pi_estimate and its absolute value difference from math.pi:
# abs(math.pi-4*pi_estimate).
def myPi(n):
    pi_estimate = 0.0
    sign = 1.0
    for count in range(n):
        term = sign / (2 * count + 1)
        pi_estimate = pi_estimate + term
        sign = -sign

    pi = print(4*pi_estimate)
    return (pi)
myPi(1000000)
