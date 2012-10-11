from LinkedList import List

import unittest

'''
Question

        Implement an algorithm to delete a node in the middle of a singly
        linked list. The only access given is the node to be deleted.

Solution

        The trick is to copy the data of the next node to the current node
        and delete the next node instead. This approach will fail if the
        node to be deleted is at the end of the list. A possible
        improvement for the list would be to make use of a dummy or
        sentinel nodel.

        Time Complexity O(1)
        Space Complexity O(1)
'''
def deleteNode(node):

        if (node == None or node.next == None):
                return # or raise an exception

        node.data = node.next.data
        node.next = node.next.next

class Test(unittest.TestCase):

        def setUp(self):
                self.list = List()

        def testDeleteNode(self):
                self.list.insert(5)
                self.list.insert(4)
                node = self.list.insert(3)
                self.list.insert(2)
                self.list.insert(1)

                deleteNode(node)
                self.assertEqual(self.list.toList(), [1, 2, 4, 5])

        def testFailure(self):
                node = self.list.insert(3)
                self.list.insert(2)
                self.list.insert(1)

                deleteNode(node)
                self.assertEqual(self.list.toList(), [1, 2, 3])




if __name__ == '__main__':
        unittest.main()



