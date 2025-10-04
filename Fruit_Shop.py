# Write a program that reads:

#- A fruit name,
#- A day of the week,
# - A quantity (float),
# and calculates the total price for that quantity of the fruit on the given day.


fruit = input()
week_day = input()
quantity = float(input())

price = 0

valid_fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
valid_week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if fruit not in valid_fruits:
    print('error')
else:

    if week_day not in valid_week_day:
        print('error')
    else:

        if week_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            if fruit == 'banana':
                price = 2.50
            elif fruit == 'apple':
                price = 1.20
            elif fruit == 'orange':
                price = 0.85
            elif fruit == 'grapefruit':
                price = 1.45
            elif fruit == 'kiwi':
                price = 2.70
            elif fruit == 'pineapple':
                price = 5.50
            elif fruit == 'grapes':
                price = 3.85
        elif week_day in ["Saturday", "Sunday"]:
            if fruit == 'banana':
                price = 2.70
            elif fruit == 'apple':
                price = 1.25
            elif fruit == 'orange':
                price = 0.90
            elif fruit == 'grapefruit':
                price = 1.60
            elif fruit == 'kiwi':
                price = 3.00
            elif fruit == 'pineapple':
                price = 5.60
            elif fruit == 'grapes':
                price = 4.20

        if price > 0:
            total_price = price * quantity
            print(f"{total_price:.2f}")
