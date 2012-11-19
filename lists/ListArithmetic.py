from LinkedList import List
import unittest

'''
Question

        You have two numbers represented by a linked list, where each
        node contains a single digit. The digits are stored in reversed
        order, such that the 1's digit is at the head of the list. Write
        a function that adds the two numbers and returns the result as a
        linked list

Solution

        This problem can be solved with pencil-and-paper addition. First
        the 1's digits are added, the result is inserted into the result
        list, then the 2's digits are added, etc. In each step a
        possible carry has to be extracted as well.

        Time Complexity O(n)
        Space Complexity O(n)
'''
def add(list1, list2):

        result = List()
        a = list1.head
        b = list2.head
        carry = 0

        while (a != None and b != None):
                value = a.data + b.data + carry
                result.append(value % 10)
                carry = value / 10
                a = a.next
                b = b.next

        while (a != None):
                value = a.data + carry
                result.append(value % 10)
                carry = value / 10
                a = a.next
                
        while (b != None):
                value = b.data + carry
                result.append(value % 10)
                carry = value / 10
                b = b.next

        if (carry != 0):
                result.append(carry)

        return result

class ListArithmeticTest(unittest.TestCase):

        def testAdd(self):

                list1 = List()
                list2 = List()

                list1.insert(6)
                list1.insert(1)
                list1.insert(7)

                list2.insert(2)
                list2.insert(9)
                list2.insert(5)
                
                result = add(list1, list2)
                self.assertEqual(result.toList(), [2, 1, 9])

                list1 = List()
                list2 = List()

                list1.insert(3)
                
                list2.insert(7)
                list2.insert(7)

                result = add(list1, list2)
                self.assertEqual(result.toList(), [0, 8])

if __name__ == '__main__':
        unittest.main()
