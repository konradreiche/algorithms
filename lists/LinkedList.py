'''
Question

        Implement a singly linked list.

Solution:

        The implementation is based on a node object which is used for the
        entries of the linked list. A head attribute in the List wrapper
        class allows to access the beginning of the list.
'''
class Node(object):

        def __init__(self, data):
                self.data = data
                self.next = None

class List(object):

        def __init__(self):
                self.head = None

        def insert(self, data):

                '''Time Complexity O(1)'''

                node = Node(data)
                if self.head is None:
                        self.head = node
                else:
                        node.next = self.head
                        self.head = node

        def delete(self, data):

                '''Time Complexity O(n)'''

                current = self.head
                prev = None
                while current is not None:
                        if current.data == data:
                                if current == self.head:
                                        self.head = current.next
                                else:
                                        prev.next = current.next
                                break
                        else:
                                prev = current
                                current = current.next

        def toList(self):

                result = []
                current = self.head
                while current is not None:
                        result.append(current.data)
                        current = current.next

                return result

        def __str__(self):

                result = ''
                current = self.head
                while current is not None:
                        result += str(current.data) + ' '
                        current = current.next

                return result
