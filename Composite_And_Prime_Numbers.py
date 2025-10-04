#Write a program that reads an integer number and determines if it is prime, composite, or neither.
#- Numbers less than 2 are neither prime nor composite.
#- A prime number has no divisors other than 1 and itself.
#- A composite number has at least one divisor other than 1 and itself.



number = int(input("Enter your number: "))

if number < 2:
    print(f'Your number {number} is neither prime nor composite number. ')
else:
    for i in range(2, number):
        if number % i == 0:
            print(f'Your number {number} is a composite number.')
            break
    else:
        print(f'Your number {number} is a prime number.')
