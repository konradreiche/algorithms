from LinkedList import List

import unittest

'''
Question

        Write code to partition a linked list, such that for a given value
        x all nodes less than x come before all nodes greater or equal
        than x.

Solution

        Array shifts are considered to be an expensive operation. For a
        linked list this can be solved by simply creating two new lists
        and merging them in the end.

        This solution can be enhanced by keeping track of the last list
        elements in order to do the merging in one step.

        Time Complexity O(n)
        Space Complexity O(n)
'''
def partition(list, x):

        if (list.head == None):
                return

        leftList = List()
        rightList = List()

        current = list.head
        while True:

                if (current.data < x):
                        leftList.insert(current.data)
                else:
                        rightList.insert(current.data)

                current = current.next

                if (current == None):
                        break

        lastLeftListNode = leftList.head
        while (lastLeftListNode.next != None):
                lastLeftListNode = lastLeftListNode.next

        lastLeftListNode.next = rightList.head
        list.head = leftList.head

class Test(unittest.TestCase):

        def testPartition(self):

                list = List()
                list.insert(9)
                list.insert(7)
                list.insert(50)
                list.insert(6)
                list.insert(5)
                list.insert(2)
                list.insert(3)

                partition(list, 8)
                self.assertEqual(list.toList(), [7, 6, 5, 2, 3, 9, 50])

                list = List()
                list.insert(1)

                partition(list, 2)
                self.assertEqual(list.toList(), [1])

        def testPartitionEmptyList(self):

                list = List()

                partition(list, 8)
                self.assertEqual(list.toList(), [])

if __name__ == '__main__':
        unittest.main()               
