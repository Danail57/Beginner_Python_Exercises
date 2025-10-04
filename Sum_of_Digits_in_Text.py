# Write a program that reads a string and calculates the sum of all digits found within the string.

text = input()
total_sum = 0

digits_indices = []
for symbol in text:
    if symbol.isdigit():
        total_sum += int(symbol)
print(f'The sum of digits is {total_sum}')
