import unittest

'''
Question

        Assume you have a method isSubstring which checks if one word is
        a substring of another. Given two strings, s1 and s2, write code
        to check if s2 is a rotation of s1 using only one call to
        isSubgstring, e.g., "waterbottle" is a rotation of
        "erbottlewat".

Solution

       Depended on where the rotation point is in s2 the string can be
       divided into two parts, x and y.

       s1 = xy = waterbottle
       x = wat
       y = erbottle
       s2 = yx

       Regardless of where the division happens, yx will always be a
       substring of xyxy. Hence, s2 is a rotation of s1 if s2 is a
       substring of s1s1.

       Time Complexity O(1)
       Space Complexity O(n)
'''
def isRotation(s1, s2):

        if (len(s1) == len(s2) and len(s1) > 0):

                s1s1 = s1 + s1
                return s2 in s1s1

        return False

class RotationTest(unittest.TestCase):

        def testIsRotation(self):

                s1 = "waterbottle"
                s2 = "erbottlewat"
                self.assertTrue(isRotation(s1, s2))

                s1 = "12345"
                s2 = "23415"
                self.assertFalse(isRotation(s1, s2))

if __name__ == '__main__':
        unittest.main()
