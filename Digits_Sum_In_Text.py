# Write a program that reads a list of integers and checks whether
# the sum of the digits at even indices is equal to the sum of the digits at odd indices.

digits = list(map(int,input().split()))
total_sum_even = 0
total_sum_odd = 0
total_sum = 0

for index, digit in enumerate(digits):
    if index % 2 == 0:
        total_sum_even += digit
    else:
        total_sum_odd += digit

if total_sum_even == total_sum_odd:
    print('Yes')
    print(f'Sum = {total_sum_even}')
else:
    diff = abs(total_sum_even - total_sum_odd)
    print('No')
    print(f'Diff = {diff}')
