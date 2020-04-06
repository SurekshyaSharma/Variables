# [H6-2] (patterns2.py) (2 points each) Write a program that reads an int N >= 0, then prints out each of the
# following  patterns of *. If you do NOT use the string repetition operator * in either problem, you will earn 0.25
# points of Extra Credit for each.  Also, each pattern must be output via a single function call to the given named
# function with single parameter N. Examples for N==4follow, with explanations of how the displayed diagram reflects
# this value of N

STAR = "*"
SPACE = " "


def triangle(N):
    for row in range(N):
        for r in range(0, row):
            print(SPACE, end="")
        for col in range(N-row, 0, -1):
            print(STAR, end='')
        print()
    print("----------------------------------------------")


def hollow_box(N):
    for row in range(N):
        for col in range(N):
            if row == 1 or row == N or col == 1 or col == N:
                 print(STAR, end="")
        print()
    print("-------------------------------------------")
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if (row == 1 or row == N or
                    col == 1 or col == N):
                print(STAR, end="")
            else:
                print(" ", end="")

        print()


def main():

    N = int(input("Enter the number: "))
    triangle(N)
    hollow_box(N)


main()
