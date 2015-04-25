import sys


def find_factors(num):
    """Take a number, and print a list of the factors."""
    divisors = list(range(2, int(num)))
    factors = [1]
    for d in divisors:
        if num % d == 0:
            factors.append(d)
    factors.append(num)
    print(factors)

if __name__ == '__main__':
    find_factors(int(sys.argv[1]))
