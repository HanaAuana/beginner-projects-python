import sys


def print_bottles(max, min):
    """Print the lyrics to max Bottles of Beer on the wall."""
    for num in range(max, min - 1, -1):
        if num == 1:
            print('1 bottle of beer on the wall, 1 bottle of beer')
            print('Take one down, pass it around, no more bottles of beer on the wall'.format(num-1))
        else:
            print('{0} bottles of beer on the wall, {0} bottles of beer'.format(num))
            if num - 1 == 1:
                print('Take one down, pass it around, 1 bottle of beer on the wall')
            else:
                print('Take one down, pass it around, {} bottles of beer on the wall'.format(num-1))
        print()
print_bottles(int(sys.argv[1]), int(sys.argv[2]))
