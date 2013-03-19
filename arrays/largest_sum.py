'''
Question

    Given an array with integers, positive and negative. Find the subarray with
    the largest sum. For example, for the array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    the contiguous subarray with the largest sum is [4, -1, 2, 1], summing up
    to 6.

Solution

    This problem is also known as maximum subarray problem can is a simplified
    model for the maximum likelihood estimation of patterns in digitized
    images. A bruteforce solution would lead to a O(n^2) time complexity.

    Kadane's algorithm scans through they values, while computing at each
    position the maximum subarray ending in that position. This subarray is
    then either empty (summing up to 0) or consists of one more element than
    the maximum subarray ending at the previous position.

    Time Complexity O(n)
'''
import unittest


def largest_sum(array):

    max_ending_here = 0
    max_so_far = 0

    start = 0
    end = 0

    for i, number in enumerate(array):

        if (max_ending_here + number) > 0:
            if max_ending_here == 0:
                start = i

            max_ending_here += number

        else:
            max_ending_here = 0

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            end = i + 1

    return array[start:end]


class LargestSumTest(unittest.TestCase):

    def test_largest_sum(self):
        self.assertEqual(largest_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])
        self.assertEqual(largest_sum([-2, -1, -5, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(largest_sum([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
