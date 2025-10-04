# Write a program that reads a string and finds the indices of all lowercase letters in the text.

text = input()

lowercase_indices = []
for index in range(len(text)):
    if text[index].islower():
        lowercase_indices.append(index)
print(lowercase_indices)
