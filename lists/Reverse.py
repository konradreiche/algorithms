import unittest

from LinkedList import List

'''
Question

        Reverse a simply linked list.

Solution

        The list is iterating while managing three variables holding the
        previous, current and next node in the linked list and updating
        their values.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def reverse(list):

        current = list.head
        temp = None
        prev = None
        while current is not None:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

        list.head = prev

class TestReverseList(unittest.TestCase):

        def setUp(self):
                self.list = List()

        def testReverse(self):

                self.list.insert(3)
                self.list.insert(7)
                self.list.insert(11)
                self.list.insert(13)
                self.list.insert(17)
                self.assertEqual(self.list.toList(), [17, 13, 11, 7, 3])
                reverse(self.list)
                self.assertEqual(self.list.toList(), [3, 7, 11, 13, 17])

if __name__ == '__main__':
        unittest.main()
