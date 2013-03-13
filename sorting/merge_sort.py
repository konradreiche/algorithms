import unittest

"""
Question

    Implement a simple but inefficient merge sort.

Solution

    This implementation uses recursion. Most of the work is done in the merge
    function combining two sorted arrays into a larger sorted array.

    Time Complexity O(n * log n)
"""


def merge_sort(data):

    if len(data) < 2:
        return data

    mid = len(data) / 2
    left = [0] * mid  # new int[mid]
    right = [0] * (len(data) - mid)  # new int[data.length - mid]

    left = data[0:len(left)]
    right = data[mid:mid + len(right)]

    merge_sort(left)
    merge_sort(right)
    return merge(data, left, right)


def merge(dest, left, right):
    dind = 0
    lind = 0
    rind = 0

    while lind < len(left) and rind < len(right):
        if left[lind] <= right[rind]:
            dest[dind] = left[lind]
            dind += 1
            lind += 1
        else:
            dest[dind] = right[rind]
            dind += 1
            rind += 1

    # copy rest of the remaining array
    while lind < len(left):
        dest[dind] = left[lind]
        dind += 1
        lind += 1

    while rind < len(right):
        dest[dind] = right[rind]
        dind += 1
        rind += 1

    return dest


class MergeSortTest(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort([10, 1, 4, 2, 3, 8]), [1, 2, 3, 4, 8, 10])
        self.assertEqual(merge_sort([]), [])

if __name__ == '__main__':
    unittest.main()
