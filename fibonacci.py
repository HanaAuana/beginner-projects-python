def fibonacci(num):
    """Return the num-th number in the fibonacci sequence."""
    if num == 0:
        return 0
    else:
        result = 1
        n_1 = 0
        n_2 = 1
        for i in range(num - 1):
            result = n_1 + n_2
            n_1 = n_2
            n_2 = result
        return result
