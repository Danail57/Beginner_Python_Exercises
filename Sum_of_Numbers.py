# Write a program that reads a number as a string, calculates the sum of its digits, and prints the result.

number = input("Enter a number: ")
sum_of_digits = sum(map(int, number))
print(f'The sum of the digits is {sum_of_digits}.')
