def check_pythagorean(num1, num2, num3):
    """Verify whether the 3 parameters are a Pythagorean Triple."""

    if num1 <= 0 or num2 <= 0 or num3 <= 0:
        return False

    hypotenuse = max(num1, num2, num3)
    if num1 == hypotenuse:
        return (num1 ** 2 == (num2 ** 2 + num3 ** 2))
    elif num2 == hypotenuse:
        return (num2 ** 2 == (num1 ** 2 + num3 ** 2))
    else:
        return (num3 ** 2 == (num1 ** 2 + num2 ** 2))

while True:
    num1 = input('Enter a side: ')
    num2 = input('Enter another side: ')
    num3 = input('Enter the last side: ')
    if check_pythagorean(int(num1), int(num2), int(num3)):
        print('{}, {}, and {} are a Pythagorean Triple'.format(num1, num2, num3))
    else:
        print('{}, {}, and {} are not a Pythagorean Triple'.format(num1, num2, num3))

    again = input('Do you want to check another? Type yes to continue: ')
    if again.lower() not in ('yes', 'y', 'continue'):
        break
