from src import bellman_ford, get_bellman_ford_path
import unittest


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        edges = [
            [0, 1, 4],
            [0, 2, 3],
            [1, 2, 1],
            [1, 3, 1],
            [1, 4, 5],
            [2, 5, 2],
            [4, 6, 2],
            [5, 4, 1],
            [5, 6, 4]
        ]
        num_node = 7
        start = 0
        dist, _ = bellman_ford(edges, num_node, start)
        expected_dist = [0, 4, 3, 5, 6, 5, 8]
        self.assertEqual(dist, expected_dist)

    def test_get_bellman_ford_path(self):
        edges = [
            [0, 1, 4],
            [0, 2, 3],
            [1, 2, 1],
            [1, 3, 1],
            [1, 4, 5],
            [2, 5, 2],
            [4, 6, 2],
            [5, 4, 1],
            [5, 6, 4]
        ]
        num_node = 7
        start = 0
        _, prev = bellman_ford(edges, num_node, start)
        path_to_6 = get_bellman_ford_path(prev, 6)
        print(path_to_6)
        self.assertEqual(path_to_6, [0, 2, 5, 4, 6])
        path_to_0 = get_bellman_ford_path(prev, 0)
        print(path_to_0)
        self.assertEqual(path_to_0, [0])

    def test_bellman_ford_negative(self):
        edges = [
            [0, 1, 2],
            [0, 3, 4],
            [1, 2, 3],
            [2, 3, 5],
            [2, 5, 2],
            [4, 2, -4],
            [5, 4, 1],
        ]
        num_node = 6
        start = 0
        dist, prev = bellman_ford(edges, num_node, start)
        self.assertEqual(dist, -1)
        self.assertEqual(prev, -1)


if __name__ == "__main__":
    unittest.main()
