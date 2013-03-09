from graph import Graph

from Queue import Queue
import unittest

"""
Question

    Implement Depth First Search (DFS).

Solution

    Depth-first explores edges out of the most recently discovered node n that
    still has unexplored edges leaving it. Once all of n's edges have been
    explored, the search "backtracks" to explore edges leaving the node from
    which n was discovered.

    Time Complexity: O(V + E)

"""


def depth_first_search(node):

    traversal = []
    if not node:
        return []

    traversal.append(node.value)  # visit(node)
    node.visited = True
    for n in node.adjacent:
        if not n.visited:
            traversal = traversal + depth_first_search(n)

    return traversal


"""
Question

    Implement Breadth First Search (BFS).

Solution

    Breadth-first search systematically explores the edges of the graph to
    "discover" every node that is reachable from the source node s. In BFS
    first all adjacent nodes of a given node r are visited before continuing to
    visit r's "grandchildren". An iterative implementation works just fine, the
    key to remember here is the use of queue.

    Time Complexity: O(V + E)
"""


def breadth_first_search(node):
    queue = Queue()
    node.visited = True
    traversal = [node.value]  # visit(node)
    queue.put(node)

    while not queue.empty():
        r = queue.get()
        for n in r.adjacent:
            if not n.visited:
                traversal.append(n.value)  # visit(node)
                n.visited = True
                queue.put(n)

    return traversal


class TraversalTest(unittest.TestCase):

    def test_depth_first_search(self):
        graph = Graph()
        graph.add_nodes(['A', 'B', 'C', 'D', 'E'])
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        graph.add_edge('B', 'D')
        graph.add_edge('D', 'E')
        self.assertEquals(depth_first_search(graph.nodes['A']),
                          ['A', 'B', 'C', 'D', 'E'])
        graph.reset_visits()

    def test_breadth_first_search(self):
        graph = Graph()
        graph.add_nodes(['A', 'B', 'C', 'D', 'E'])
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        graph.add_edge('B', 'D')
        graph.add_edge('D', 'E')
        self.assertEquals(breadth_first_search(graph.nodes['A']),
                          ['A', 'B', 'C', 'D', 'E'])
        graph.reset_visits()

if __name__ == '__main__':
    unittest.main()
