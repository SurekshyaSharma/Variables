# 1. Define a function delete_digits(mystring). You don't have to call it.When called, it should return a copy of
# mystring with all characters converted to lowercase, followed by the removal of any digits '0123456789'.


print("------------------------------------------------------------------")
#
# 2. What should the values of X and Y be, so that the following code prints the 'd' found inside one of the elements of
# alist?
#
alist = [['47a', '47b'], '47c', '47d', [['47e', '47f'], '47g']]
# print(alist)
print("Question2")
print(alist[2][2])

# # Then write another print(...) statement that prints the the 'b' inside of alist, by use of indexing to its specific
# # location within alist.
print(alist[0][1][2])

print("------------------------------------------------------------------")

# 3. Write Python statements which assign values to a and b, resulting in a reference diagram like this:
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)
print("------------------------------------------------------------------")
a = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
print("Before", a)
a[2].append(400)
a[1].append(40)

print(a)

print("------------------------------------------------------------------")
# outside_list = []
# for i in range(0, 5):
#     inside_list = []
#     inside_list.append(i)
#     inside_list.append(i + 1)
#     outside_list.append(inside_list)
#
#     # you can access any inside_list from the outside_list and append
#     outside_list[1].append(100)
#     print(outside_list)
# print("------------------------------------------------------------------")
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])

print(n_list[1][3])
print(n_list[0][3])
print("------------------------------------------------------------------")


def delete(s):
    vowels = "aeiou"
    string = ""
    print(s)
    for ch in s:
        if ch  not in vowels:
            string = string + ch
    return string

print("Ommiting Vowels from the string:", delete("aitidde"))


print("-----------------------------------------------------------------")
#
# def delete_digits(s):
#     digits = "0123456789"
#     string_without_digits = ""
#     for eachChar in s:
#         if eachChar not in digits:
#             string_without_digits = string_without_digits + eachChar
#     return string_without_digits.lower()
#
#
# print(delete_digits("cCDDm1234psci"))
# print(delete_digits("aAbEef234GIijOopUus"))



def delete_digits(s):
    digits = "0123456789"
    string_without_digits = ""
    # print(s.lower())

    for eachChar in s.lower():
        if eachChar not in digits:
            string_without_digits = string_without_digits + eachChar
    return string_without_digits


# print(delete_digits("cCDDm1234psci"))
# print(delete_digits("aAbEef234GIijOopUus"))


def delete_digits(s):
    digits='0123456789'
    string_without_digits=""
    for ch in s.lower():
        if ch not in digits:
            string_without_digits = string_without_digits + ch
    return string_without_digits


print(delete_digits("cCDDm1234psci"))
print(delete_digits("aAbEef234GIijOopUus"))
