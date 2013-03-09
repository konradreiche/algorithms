import unittest

"""
Question

        Write a simple binary search tree.

Solution

        For the implementation tree nodes are used. The root is stored as
        an attribute in the tree data structure. If it is null the tree is
        empty.
"""


class TreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self):
        self.root = None

    """
    Question

            Implement preorder traversal.
    """

    def preorder(self, node):
        if not node:
            return
        # visit(node)
        self.preorder(node.left)
        self.preorder(node.right)

    """
    Question

            Implement inorder traversal.
    """

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        # visit(node)
        self.inorder(node.right)

    """
    Question

            Implement postorder traversal.
    """

    def postorder(self, node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        # visit(node)

    def insert(self, data):
        """Time Complexity O(n)"""

        new = TreeNode(data)
        current = self.root

        if current is None:
            self.root = new
            return

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new
                    return
                else:
                    current = current.left
            elif data == current.data:
                return
            else:
                if current.right is None:
                    current.right = new
                    return
                else:
                    current = current.right


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def testInsert(self):

        try:
            self.tree.insert(11)
            self.tree.insert(7)
            self.tree.insert(13)
            self.tree.insert(5)
            self.tree.insert(17)
            self.tree.insert(3)
        except Exception, e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()