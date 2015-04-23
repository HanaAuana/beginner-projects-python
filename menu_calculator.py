from collections import Counter

menu = [3.5,
        2.5,
        4.0,
        3.5,
        1.75,
        1.50,
        2.25,
        3.75,
        1.25
        ]


def parse_order(order):
    """Take a string, and return a dict of the order."""
    numbers = [int(n) for n in list(order)]
    counts = Counter(numbers)
    return dict(counts)


def take_orders():
    while True:
        order = input("May I take your order?")
        counts = parse_order(order)
        total = 0
        for number, count in counts.items():
            total += (count * menu[number - 1])
        print("Total is ${:.2f}".format(total))
        again = input('Do you have another order? Type yes to continue: ')
        if again.lower() not in ('yes', 'y', 'continue'):
            break

if __name__ == '__main__':
    take_orders()
