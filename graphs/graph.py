import unittest

"""
Question

    Implement a graph data structure.

Solution

    The graph is implemented by using a seperate Node class which is used to
    store the value and adjacent nodes. The graph itself is implemented by
    using a dictionary. This way the nodes can still be accessed by their
    values.

"""


class Node(object):

    def __init__(self, value):
        self.adjacent = []
        self.value = value
        self.visited = False


class Graph(object):

    def __init__(self):
        self.nodes = {}

    def add_nodes(self, nodes):
        """Time Complexity O(n)"""

        for node in nodes:
            self.nodes[node] = Node(node)

    def add_edge(self, node1, node2):
        """Time Complexity O(1)"""

        self.nodes[node1].adjacent.append(self.nodes[node2])
        self.nodes[node2].adjacent.append(self.nodes[node1])

    def reset_visits(self):
        for node in self.nodes.values():
            node.visited = False


class GraphTest(unittest.TestCase):

    def test_add_nodes(self):
        graph = Graph()
        graph.add_nodes(['Portugal', 'Spain', 'France', 'Germany'])
        graph.add_nodes(['Belgium', 'Netherlands', 'Italy'])
        self.assertTrue('Netherlands' in graph.nodes.keys())

    def test_add_edge(self):
        graph = Graph()
        graph.add_nodes(['A', 'B', 'C'])
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'C')

        node_a = graph.nodes['A']
        node_b = graph.nodes['B']
        node_c = graph.nodes['C']

        self.assertEquals(node_a.adjacent, [node_c])
        self.assertEquals(node_b.adjacent, [node_c])
        self.assertEquals(node_c.adjacent, [node_a, node_b])

if __name__ == '__main__':
    unittest.main()
