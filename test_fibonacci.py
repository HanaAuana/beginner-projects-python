import fibonacci
import unittest


class KnownValues(unittest.TestCase):
    known_fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21]

    def test_fib_known_value(self):
        """fibonacci should return known value from known input list."""
        for i in range(0, len(self.known_fibs)):
            result = fibonacci.fibonacci(i)
            self.assertEqual(self.known_fibs[i], result)


if __name__ == '__main__':
    unittest.main()
