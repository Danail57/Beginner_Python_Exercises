# Write a program that reads an integer and prints whether each number from 1 to that number (inclusive) is “special” or not.
# A number is considered special if the sum of its digits is 5, 7, or 11.
# Note: ANother decision

number = int(input())
for current_number in range(1, number + 1):
    digits_sum = sum(int(digit) for digit in str(current_number))
    is_special = digits_sum in (5, 7, 11)
    print(f'{current_number} -> {is_special}')
