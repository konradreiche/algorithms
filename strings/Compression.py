from cStringIO import StringIO
import unittest

'''
Question

        Implement a method to perform basic string compression based on
        the counts of repeated characters. For example, the string
        aabccccaaa would become a2b1c4a3. If the "compressed" string
        would not become smaller than the original string, the method
        should return the original string.

Solution 1

        The input string is iterated one character at a time. Two
        variables keep track of the current characters. As long as both
        variables are equal a counter is incremented. If both variables
        are not equal anymore the character sequence is compressed into
        the result string.
        
        In the end a length comparison is made on which it is decided
        whether the "compressed" string or the original string is
        returned.

        With p being the length of the input string and k the number of
        character sequences this approach is inefficient, since the
        string concatenation operates in O(n^2).

        Time Complexity O(p + k^2)
        Space Complexity O(p)
'''
def compress(string):
        
        if len(string) == 0:
                return string

        result = ''
        counter = 1
        last = ''
        current = string[0]
        for i in range(1, len(string)):
                last = current
                current = string[i]
                if (last == current):
                        counter += 1
                else:
                        result += last + str(counter)
                        counter = 1

        result += last + str(counter)
        if len(result) >= len(string):
                return string
        else:
                return result

'''
Solution 2

        Using a string buffer is more efficient. In Java this would be
        the StringBuilder class. In Python something similar is the
        StringIO class a wrapper for the C implementation cStringIO.

        In addition the compression size can be computed beforehand in
        order to decide whether the string will be larger before
        compressing the string. Obviously the number encoding the number
        of repetitions can grow larger than one character.

        Time Complexity O(n)
        Space Complexity O(n)
'''
def compressBetter(string):
        
        size = computeCompressionSize(string)
        if size >= len(string):
                return string

        result = StringIO()
        counter = 1
        last = ''
        current = string[0]
        for i in range(1, len(string)):
                last = current
                current = string[i]
                if (last == current):
                        counter += 1
                else:
                        result.write(last)
                        result.write(str(counter))
                        counter = 1

        result.write(last)
        result.write(str(counter))
        return result.getvalue()
        

def computeCompressionSize(string):

        if len(string) == 0:
                return 0

        size = 0
        counter = 1
        last = string[0]
        for i in range(1, len(string)):
                if (last == string[i]):
                        counter += 1
                else:
                        last = string[i]
                        size += 1 + len(str(counter))

        return size + 1 + len(str(counter))

'''
Solution 3

        If a string buffer is not allowed the computed compression size
        can be used for allocate a character array with the appropriate
        size for the compressed string.

        Time Complexity O(n)
        Space Complexity O(n)
'''

class TestCompression(unittest.TestCase):

        def testCompression(self):
                
                self.assertEqual(compress('aabccccaaa'), 'a2b1c4a3')
                self.assertEqual(compress('abc'), 'abc')
                self.assertEqual(compress(''), '')
                self.assertEqual(compress('a'), 'a')
                self.assertEqual(compress('Hello Berlin!'), 'Hello Berlin!')
                self.assertEqual(compress('aaaaaaaaaa'), 'a10')
                

        def testCompressionBetter(self):
                
                self.assertEqual(compressBetter('aabccccaaa'), 'a2b1c4a3')
                self.assertEqual(compressBetter('abc'), 'abc')
                self.assertEqual(compressBetter(''), '')
                self.assertEqual(compressBetter('a'), 'a')
                self.assertEqual(compressBetter('Hello Berlin!'), 'Hello Berlin!')
                self.assertEqual(compressBetter('aaaaaaaaaa'), 'a10')

        def testComputeCompressionSize(self):

                self.assertEqual(computeCompressionSize('aabccccaaa'), len('a2b1c4a3'))
                self.assertEqual(computeCompressionSize('abc'), len('a1b1c1'))
                self.assertEqual(computeCompressionSize(''), len(''))
                self.assertEqual(computeCompressionSize('a'), len('a1'))
                self.assertEqual(computeCompressionSize('Hello Berlin!'), len('H1e1l2o1 1B1e1r1l1i1n1!1'))
                self.assertEqual(computeCompressionSize('aaaaaaaaaa'), len('a10'))

if __name__ == '__main__':
        unittest.main()

