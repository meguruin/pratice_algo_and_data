from src import warshall_floyd, get_warshall_floyd_path
import unittest


class TestWarshallFloyd(unittest.TestCase):
    def setUp(self):
        self.num_nodes = 4
        self.edge_list = [
            [0, 1, 10],
            [0, 3, 100],
            [1, 3, 1000],
            [2, 1, 1],
            [2, 3, 10000],
            [3, 0, 5],
        ]
        # make adjacent_matrix
        self.adjacent_list = [[float("inf") for j in range(self.num_nodes)] for i in range(self.num_nodes)]
        for edge in self.edge_list:
            n1, n2, w = edge
            self.adjacent_list[n1][n2] = w

    def test_warshall_floyd(self):
        dist, _ = warshall_floyd(self.adjacent_list)
        expected_dist = [
            [0, 10, float("inf"), 100],
            [1005, 0, float("inf"), 1000],
            [1006, 1, 0, 1001],
            [5, 15, float("inf"), 0]
        ]
        self.assertEqual(dist, expected_dist)

    def test_get_warshall_floyd_path(self):
        _, prev = warshall_floyd(self.adjacent_list)
        path_from_2_to_0 = get_warshall_floyd_path(prev, 2, 0)
        self.assertEqual(path_from_2_to_0, [2, 1, 3, 0])


if __name__ == "__main__":
    unittest.main()
