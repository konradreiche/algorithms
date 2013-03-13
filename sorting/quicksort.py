import unittest

"""
Question

    Implement a simple but inefficient quicksort.

Solution

    Since the starting array is scanned twice and new arrays are allocated,
    this implementation is not very efficient.

    Time Complexity O(n * log n)
"""


def quicksort(data):

    if len(data) < 2:
        return data

    pivot_index = len(data) / 2
    pivot_value = data[pivot_index]

    left_count = 0

    # count how many elements are less than the pivor
    for i in range(len(data)):
        if data[i] < pivot_value:
            left_count += 1

    left = [0] * left_count  # new int[leftCount]
    right = [0] * (len(data) - left_count - 1)  # new int[data.length - leftCount - 1]

    l = 0
    r = 0

    for i in range(len(data)):
        if i == pivot_index:
            continue

        val = data[i]

        if val < pivot_value:
            left[l] = val
            l += 1
        else:
            right[r] = val
            r += 1

    # sort the subsets
    left = quicksort(left)
    right = quicksort(right)

    # combine sorted arrays and pivot back into original  array
    return left + [pivot_value] + right


class QuicksortTest(unittest.TestCase):

    def test_quicksort(self):
        self.assertEqual(quicksort([10, 1, 4, 2, 3, 8]), [1, 2, 3, 4, 8, 10])
        self.assertEqual(quicksort([]), [])

if __name__ == '__main__':
    unittest.main()
