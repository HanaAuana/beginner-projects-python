from math import ceil

coin_weights = {"penny": 2.5,
                "nickel": 5.0,
                "dime": 2.268,
                "quarter": 5.67
                }

wrapper_capacity = {"penny": 50,
                    "nickel": 40,
                    "dime": 50,
                    "quarter": 40
                    }


def weight_to_quantity(w, denomination):
    coin_weight = coin_weights[denomination]
    return int(round(w / coin_weight))


def quantity_to_wrappers(q, denomination):
    num_wrappers = wrapper_capacity[denomination]
    return ceil(q / num_wrappers)


def pounds_to_grams(n):
    return n * 453.592

while True:
    use_grams = input('Enter g for grams or lbs for pounds')
    penny_weight = float(input('Enter the weight of your pennies: '))
    nickel_weight = float(input('Enter the weight of your nickels: '))
    dime_weight = float(input('Enter the weight of your dimes: '))
    quarter_weight = float(input('Enter the weight of your quarters: '))

    weights = [("penny", "pennies", penny_weight, 1),
               ("nickel", "nickels", nickel_weight, 5),
               ("dime", "dimes", dime_weight, 10),
               ("quarter", "quarters", quarter_weight, 25)
               ]
    total = 0
    for denomination, plural, weight, value in weights:
        # If the user entered weights in pounds, convert to grams
        if use_grams.lower() not in ('g', 'grams'):
            w = pounds_to_grams(weight)
            print('{0} lbs of {1}'.format(int(round(w)), plural))
        else:
            w = weight
            print('{0} grams of {1}'.format(int(round(w)), plural))
        quantity = weight_to_quantity(w, denomination)
        print('Number of {0}: {1}'.format(plural, quantity))
        wrappers = quantity_to_wrappers(quantity, denomination)
        print('Number of {0} wrappers needed: {1}'.format(denomination, wrappers))
        total += (quantity * value)
    print('Total value in cents: {0}. In dollars: {1}'.format(total, total / 100))

    again = input('Do you want to check another group? Type yes to continue: ')
    if again.lower() not in ('yes', 'y', 'continue'):
        break
