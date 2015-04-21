import sys


def print_table(size):
    """Print a multiplication of 'size X size' dimensions (Up to 15X15)."""

    if size > 15:
        print("WARNING: Formatting may be off due to size (", size, ")")

    numbers = range(1, size + 1)

    # Length of the largest value
    max = len(str(size * size))
    # String of "-"'s to divide each row
    row_divider = '\n    ' + '-' * ((size) * (max + 2))

    # Print header row
    print(" " * (max + 2), end='')
    for num in numbers:
        print(" {0:>{1}}|".format(num, max), end='')
    print(row_divider)

    # Each cell will be justified based on the maximum length for the table
    for row in numbers:
        print(" {0:>{1}}|".format(row, max), end='')
        for col in numbers:
            print(" {0:>{1}}|".format(row * col, max), end='')
        print(row_divider)

print_table(int(sys.argv[1]))
