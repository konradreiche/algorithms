'''
Question

    Implement a queue using stacks. The queue is defined by the functions
    enqueue and dequeue.

Solution 1

    The queue can be implemented using two stacks and making the enqueue
    operation costly.

Solution 2

    The queue can be implemented using two stacks and making the dequeue
    operation costly.
'''
import unittest
from stack import Stack


class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, element):

        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())

        self.stack1.push(element)

        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        return self.stack1.pop()


class QueueTest(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.stack1.top.data, 1)
        self.assertEqual(queue.stack1.top.next.data, 2)
        self.assertEqual(queue.stack1.top.next.next.data, 3)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), None)


if __name__ == '__main__':
    unittest.main()
