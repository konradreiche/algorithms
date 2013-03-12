import unittest

'''
Question

    Write a function that receives a list of positive integer as an input and
    returns all the pairs that sums to 100 without duplicates.

Solution

    Recursion can be used to solve this. Two loops are searching for the pairs
    that sum up to 100. If a pair is found, both numbers are removed from the
    list which is then passed to the function recursively. The recursion base
    case is when both loops have terminated. Only an empty list will be
    concatenated in this case.

    Time Complexity O(n^2)
'''


def find_hundreds(numbers):
    result = []

    for num in numbers:
        for num2 in numbers[1:]:
            if num + num2 == 100:
                numbers.remove(num)
                numbers.remove(num2)
                result.append([num, num2])
                recursion = find_hundreds(numbers)
                result = result + recursion
                return result
    return []


class FindHundredsTest(unittest.TestCase):

    def test_find_hundreds(self):
        self.assertEqual(find_hundreds([1, 98, 99]), [[1, 99]])
        self.assertEqual(find_hundreds([95, 5, 95]), [[95, 5]])
        self.assertEqual(find_hundreds([95, 5, 95, 5]), [[95, 5], [95, 5]])
        self.assertEqual(find_hundreds([1, 2, 3, 4, 5, 99]), [[1, 99]])
        self.assertEqual(find_hundreds([2, 99]), [])

if __name__ == '__main__':
    unittest.main()
