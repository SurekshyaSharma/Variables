# Write a program which reads a word, lower-cases all its letters, then prints out a square array where the first row
# contains the word, and each subsequent line is the previous line circular-shifted one place to the left.  Example
# for entered word word =="MoXiE":

word = input('Enter the string to modify: ').lower()
length = len(word)
accumulator = ''
for i in range(length):
    accumulator = word[i:] + word[:i]
    print(accumulator)




