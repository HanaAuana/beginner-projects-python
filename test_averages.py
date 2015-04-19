import averages
import unittest


class KnownValues(unittest.TestCase):
    known_means = (([1, 2, 3, 4, 5], 3.0),
                   ([4, 4, 4, 4, 4], 4.0),
                   ([10, 10, 20, 60, 70], 34.0),
                   ([6, 7, 8], 7.0),
                   ([2, 1], 1.5),
                   )

    known_medians = (([1, 2, 3, 4, 5], 3),
                     ([4, 4, 4, 4, 4], 4),
                     ([10, 10, 20, 60, 70], 20),
                     ([6, 7, 8], 7),
                     ([1, 2, 3, 4], [2, 3]),
                     )

    known_modes = (([1, 1, 2, 2, 2], 2),
                   ([1, 2, 3, 5, 5], 5),
                   ([1, 1, 1, 1, 1], 1),
                   ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
                   ([1, 2], [1, 2]),
                   )

    def test_mean_known_value(self):
        """mean should return known value from known input list."""
        for nums, value in self.known_means:
            result = averages.mean(nums)
            self.assertEqual(value, result)

    def test_median_known_value(self):
        """median should return known value from known input list."""
        for nums, value in self.known_medians:
            result = averages.median(nums)
            self.assertEqual(value, result)

    def test_mode_known_value(self):
        """mode should return known value from known input list."""
        for nums, value in self.known_modes:
            result = averages.mode(nums)
            self.assertEqual(value, result)


if __name__ == '__main__':
    unittest.main()
