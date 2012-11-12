import unittest

'''
Question

        Given an image represented by a NxN matrix, where each pixel in
        the image is 4 bytes, write a method to rotate the image by 90
        degrees. Can you do this in place?

Solution

        The easiest way is to rotate the image layer by layer. A
        circular rotation on each layer where the top edge is moved to
        the right edge, the right edge is moved to the bottom edge, the
        bottom edge is moved to the left and the left edge to the top
        edge. This swap can be implemented index by index.

        for i = 0 to n
                temp = top[i]
                top[i] = left[i]
                bottom[i] = right[i]
                right[i] = temp

        Such a swap is performed on each layer, starting from the
        outermost layer and working inwards. The other way around would
        be possible as well.


        Time Complexity O(n^2)
        Space Complexity O(1)
'''
def rotateImage(image):

        n = len(image)
        for layer in range(n/2):
                first = layer
                last = n - 1 - layer
                for i in range(first,last):
                        offset = i - first

                        # store top
                        top = image[first][i]

                        # left -> top
                        image[first][i] = image[last - offset][first]

                        # bottom -> left
                        image[last - offset][first] = image[last][last - offset]

                        # right -> bottom
                        image[last][last - offset] = image[i][last]

                        # top -> right
                        image[i][last] = top

        return image


class TestRotateImage(unittest.TestCase):

        def testRotateImage(self):

                image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                rotate = rotateImage(image)
                self.assertEqual(rotate, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

if __name__ == '__main__':
        unittest.main()
