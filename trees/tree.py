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

    def preorder_iterative(self, node):
        parent_stack = []
        while parent_stack or node:
            if node is not None:
                parent_stack.append(node)
                # visit(node)
                node = node.left
            else:
                node = parent_stack.pop()
                node = node.right

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

    def inorder_iterative(self, node):
        parent_stack = []
        while parent_stack or node:
            if node is not None:
                parent_stack.append(node)
                node = node.left
            else:
                node = parent_stack.pop()
                # visit(node)
                node = node.right

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

    def postorder_iterative(self, node):
        if not node:
            return
        node_stack = [node]
        prev = None
        while node_stack:
            curr = node_stack[-1]  # stack.peek()
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    node_stack.append(curr.left)
                elif curr.right:
                    node_stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    node_stack.append(curr.right)
            else:
                # visit(curr)
                node_stack.pop()
            prev = curr

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
