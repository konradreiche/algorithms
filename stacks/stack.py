import unittest

'''
Question

        Implement a stack.

Solution

        The stack data structures is implemented by using the same node
        class which was used for the linked list.
'''
class Node(object):

        def __init__(self, data):
                self.data = data
                self.next = None

class Stack(object):

       def __init__(self):
               self.top = None

       def empty(self):
           return self.top == None

       def push(self, data):

               '''Time Complexity O(1)'''

               node = Node(data)
               node.next = self.top
               self.top = node

       def pop(self):

               ''' Time Complexity O(1)'''

               if self.top is None:
                       return None

               data = self.top.data
               self.top = self.top.next
               return data

class TestStack(unittest.TestCase):

        def setUp(self):
                self.stack = Stack()

        def testPush(self):
                self.assertEqual(self.stack.top, None)
                self.stack.push(3)
                self.assertEqual(self.stack.top.data, 3)
                self.stack.push(7)
                self.assertEqual(self.stack.top.data, 7)

        def testPop(self):
                self.stack.push(3)
                self.stack.push(7)
                self.assertEqual(self.stack.pop(), 7)
                self.assertEqual(self.stack.pop(), 3)
                self.assertEqual(self.stack.pop(), None)


if __name__ == '__main__':
        unittest.main()
