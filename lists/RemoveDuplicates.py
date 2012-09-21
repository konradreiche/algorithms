from LinkedList import List

'''
Question

        Write code to remove duplicates from an unsorted list. How would
        you solve this problem if a temporary buffer is not allowed?

Solution 1

        The temporary buffer can be realized by using a hash table.

        Space Complexity O(n)
        Time Complexity O(n)
'''

def removeDuplicates(list):

        table = dict()
        current = list.head
        prev = None
        while current is not None:
                if table.get(current.data, False):
                        prev.next = current.next
                else:
                        table[current.data] = True
                        prev = current
                current = current.next

'''
Solution 2

        This time without a temporary buffer. Here for each node the whole
        linked list has to be iterated until all possible duplicates are
        removed.

        Space Complexity O(1)
        Time Complexity O(n^2)

'''
def removeDuplicates2(list):

        current = list.head
        while current is not None:
                runner = current
                while runner.next is not None:
                        if (runner.next.data == current.data):
                                runner.next = runner.next.next
                        else:
                                runner = runner.next
                current = current.next

list = List()
list.insert(3)
list.insert(3)

removeDuplicates(list)
print list.head.next

list.insert(3)

removeDuplicates2(list)
print list.head.next


