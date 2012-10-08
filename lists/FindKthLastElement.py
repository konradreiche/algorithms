from LinkedList import List
import unittest

'''
Question

        Implement an algorithm to find the k-th to the last element in a
        singly linked list.

Solution 1

        If the size of the linked list is known it can be simply solved by
        iterating the list and incrementing a counter. The k-th to the
        last element can then be returned when the counter is size - k.

        Time Complexity O(n)
        Space Complexity O(1)

Solution 2

        This can be solved by using two pointers which are initialized k
        nodes apart. The first is set to the list's head and the second k
        nodes into the list. Then both are moved at the same pace until
        the second pointer hits the end of the list. The first pointer has
        then the k-th to the last element.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def findLastElement(list, k):

        if (k <= 0):
                return None

        p1 = list.head
        p2 = list.head
        for i in range(k):

                if (p2 == None):
                        return None
                
                p2 = p2.next

        if (p2 == None):
                return None

        while (p2 != None):
                p1 = p1.next
                p2 = p2.next

        return p1

class Test(unittest.TestCase):

        def setUp(self):
                self.list = List()

        def testFindLastElement(self):
                self.list.insert(5)
                self.list.insert(4)
                self.list.insert(3)
                self.list.insert(2)
                self.list.insert(1)

                result = findLastElement(self.list, 1)
                self.assertEqual(result.data, 5)

                result = findLastElement(self.list, 2)
                self.assertEqual(result.data, 4)

                result = findLastElement(self.list, 4)
                self.assertEqual(result.data, 2)


if __name__ == '__main__':
        unittest.main()

                
