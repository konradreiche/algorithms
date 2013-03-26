"""
Question

    Given the value of two nodes in a binary search tree, find the lowest
    (nearest) common ancestor. You may assume that both values already exist in
    the tree.

Solution

    Examine the current node, if value1 and value2 are both less than the
    current node's value: examine the left child. If value1 and value2 are both
    greater than the current node's value: examine the right child. Otherwise:
        the current node is the lowest common ancestor.

    Time Complexity O(log(n))
"""
from tree import Tree

import unittest


def find_lowest_common_ancestor(root, value1, value2):
    while root:
        value = root.data

        if value > value1 and value > value2:
            root = root.left
        elif value < value1 and value < value2:
            root = root.right
        else:
            return root

    return None


class LowestCommonAncestorTest(unittest.TestCase):

    def test_find_lowest_common_ancestor(self):
        tree = Tree()
        tree.insert(20)
        tree.insert(8)
        tree.insert(22)
        tree.insert(4)
        tree.insert(12)
        tree.insert(10)
        tree.insert(14)
        self.assertEqual(find_lowest_common_ancestor(tree.root, 4, 14).data, 8)

if __name__ == '__main__':
    unittest.main()
