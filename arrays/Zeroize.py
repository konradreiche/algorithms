import unittest
        
'''
Question

        Write an algorithm such that if an element in a MxN matrix is
        0, its entire row and column are set to 0.

Solution

        The row and columns cannot be set to zero during iteration,
        otherwise more rows, respectively columns are set to zero than
        intented. Two arrays can be used to track the rows and columns.

        In order to memorize which rows and columns should be set to
        zero two boolean arrays are used. After the first iteration, a
        section iteration is used for the zeroizing.

        As it is always the case the space usage can be optimized by
        using a bit vector.

        Time Complexity O(M * N)
        Space Complexity O(M + N)
'''

def zeroize(array):

        m = len(array)
        n = len(array[0])

        setRowZero = [False] * m
        setColumnZero = [False] * n

        for i in range(m):
                for j in range(n):
                        if (array[i][j] == 0):
                                setRowZero[i] = True
                                setColumnZero[j] = True

        for i in range(m):
                for j in range(n):
                        if (setRowZero[i] or setColumnZero[j]):
                                array[i][j] = 0
                                
        return array

        
class ZeroizeTest(unittest.TestCase):

        def testZeroize(self):

                array = [ [ 1, 2 ],
                          [ 3, 0 ],
                          [ 5, 6 ] ]

                valid = [ [ 1, 0 ],
                          [ 0, 0 ],
                          [ 5, 0 ] ]

                self.assertEquals(zeroize(array), valid)

if __name__ == '__main__':
        unittest.main()
