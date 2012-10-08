import unittest

'''
Question

        Write a method to replace all spaces in a string with '%20'. You
        may assume that the string has sufficient space at the end of the
        string to hold the additional characters, and that you are given
        the "true" length of the string.

Solution

        For string manipulation in place it is useful to start at the end
        and work backwards. This solution does two scans. Firstly, count
        the number of spaces to compute the final length of the string and
        secondly iterate the original string backwards and insert '%20'
        for every space occurence and for every other character simply
        copy the character.

        Time Complexity: O(n)
        Space Complexity: O(n)
'''
def replaceSpaces(string, length):

        spaceCount = 0
        for i in range(length):

                if (string[i] == ' '):
                        spaceCount += 1

        newLength = length + 2 * spaceCount
        for i in reversed(xrange(length)):

                if (string[i] == ' '):
                        string[newLength - 1] = '0'
                        string[newLength - 2] = '2'
                        string[newLength - 3] = '%'
                        newLength -= 3
                else:
                        string[newLength - 1] = string[i]
                        newLength -= 1

        return string


class TestReplaceSpaces(unittest.TestCase):

        def testReplaceSpaces(self):

                input = 'Mr. John Smith    '
                result = replaceSpaces(list(input), 14)
                result = "".join(result)
                self.assertEqual(result, 'Mr.%20John%20Smith')

                input = '   '
                result = replaceSpaces(list(input), 1)
                result = "".join(result)
                self.assertEqual(result, '%20')
                
                input = '         '
                result = replaceSpaces(list(input), 3)
                result = "".join(result)
                self.assertEqual(result, '%20%20%20')

                input = 'A   '
                result = replaceSpaces(list(input), 2)
                result = "".join(result)
                self.assertEqual(result, 'A%20')
                
                input = ' A  '
                result = replaceSpaces(list(input), 2)
                result = "".join(result)
                self.assertEqual(result, '%20A')


if __name__ == '__main__':
        unittest.main()
