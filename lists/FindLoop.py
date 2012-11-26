from LinkedList import List, Node

import unittest

'''
Question

        Given a circular linked list, implement an algorithm which
        returns the node at the beginning of the loop. A circular linked
        list is a (corrupt) linked list in which a node's next pointer
        points to an earlier node, so as to make a loop in the linked
        list.

        Example:

        Input: A -> B -> C -> D -> E
                         ^         +
                         |         |
                         +---------+

        Output: C

Solution

        After all this is the modification of a classical interview
        problem: detect if a linked list has a loop. Here the runner
        technique can be applied. Two node pointers are used. A fast
        runner takes two steps at a time and a slow runner takes one
        step at a time. Eventually both runners will meet.

        When they collide move slow runner to the head of the linked
        list. Move now slow runner and fast runner, both, at one a rate
        of one step. When they collide again both runners point to the
        beginning of the loop.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def findLoop(list):

        slow = list.head
        fast = list.head

        while (fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next
                if (slow == fast):
                        break

        if (fast == None or fast.next == None):
                return None

        slow = list.head
        while (slow != fast):
                slow = slow.next
                fast = fast.next

        return fast

class FindLoopTest(unittest.TestCase):

        def testFindLoop(self):

                list = List()
                a = Node('A')
                b = Node('B')
                c = Node('C')
                d = Node('D')
                e = Node('E')

                list.head = a
                a.next = b
                b.next = c
                c.next = d
                d.next = e
                e.next = c

                self.assertEqual(findLoop(list), c)

if __name__ == '__main__':
        unittest.main()
