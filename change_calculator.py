import math

change_options = [("quarters", 25),
                  ("dimes", 10),
                  ("nickels", 5),
                  ("pennies", 1)
                  ]

while True:
    money_due = float(input('Enter the price (in dollars: 1.50): '))
    money_paid = float(input('Enter the money paid (in dollars): '))
    change = round(money_paid - money_due, 2)
    print('{0} due in change'.format(change))
    change = change * 100

    next_coin = 0
    while change > 0 and next_coin < len(change_options):
        divisor = change_options[next_coin][1]
        number_of_coins = math.floor(change / divisor)
        print('{0} {1}'.format(number_of_coins, change_options[next_coin][0]))
        change = change % divisor
        next_coin += 1

    again = input('Need change for another amount? Type yes to continue: ')
    if again.lower() not in ('yes', 'y', 'continue'):
        break
