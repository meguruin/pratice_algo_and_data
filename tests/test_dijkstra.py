from src import dijkstra, get_dijkstra_path
import unittest


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.start = 0
        self.num_nodes = 4
        self.edge_list = [
            [0, 1, 1],
            [0, 2, 4],
            [1, 2, 2],
            [2, 3, 1],
            [1, 3, 5],
        ]
        # make adjacent_list
        self.adjacent_list = [[] for i in range(self.num_nodes)]
        for edge in self.edge_list:
            n1, n2, w = edge
            self.adjacent_list[n1].append((n2, w))

    def test_dijkstra(self):
        dist, _ = dijkstra(self.adjacent_list, self.num_nodes, self.start)
        expected_dist = [0, 1, 3, 4]
        self.assertEqual(dist, expected_dist)

    def test_get_dijkstra_path(self):
        _, prev = dijkstra(self.adjacent_list, self.num_nodes, self.start)
        path_to_2 = get_dijkstra_path(prev, 2)
        self.assertEqual(path_to_2, [0, 1, 2])
        path_to_0 = get_dijkstra_path(prev, 0)
        self.assertEqual(path_to_0, [0])


if __name__ == "__main__":
    unittest.main()
