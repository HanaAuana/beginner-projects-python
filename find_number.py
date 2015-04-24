# 1 through 1000
# Two or more digits
possible = [i for i in range(1, 1001) if i > 9]
for i in possible:
    should_add = True
    string_num = str(i)
    # Number does not contain 1 or 7
    if '7' in string_num or '1' in string_num:
        should_add = False
        continue
    # Remove if second to last digit is odd (not even)
    if int(string_num[-2:-1]) % 2 != 0:
        should_add = False
        continue
    # Remove if last digit doesn't equal number of digits in number
    if int(string_num[-1]) != len(string_num):
        should_add = False
        continue
    # Remove if first two digits are even (not odd)
    sum_of_first_two = int(string_num[0]) + int(string_num[1])
    if sum_of_first_two % 2 == 0:
        should_add = False
        continue
    # Remove if sum of digits is greater than 10 (not <= 10)
    sum_of_all = 0
    for c in string_num:
        sum_of_all += int(c)
    if sum_of_all > 10:
        should_add = False
        continue
    # Remove if number is not prime
    divisors = list(range(2, int(i ** 0.5) + 1))
    for d in divisors:
        if i % d == 0:
            should_add = False
            continue
    if should_add is True:
        print(i)
