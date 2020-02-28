
def reverse(str):
    reversed_Input= ""
    for char in str:
        reversed_Input = char + reversed_Input

    result = reversed_Input
    return result


def main():
     s = input("Enter the string to reverse: ")

     print(reverse(s))


# main()
