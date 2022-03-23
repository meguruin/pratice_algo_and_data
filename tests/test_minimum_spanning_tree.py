from src import prim, kruskal
import unittest


class TestMinimumSpanningTree(unittest.TestCase):
    def setUp(self):
        self.edge = [
            [[1, 10], [4, 30]],
            [[0, 10], [2, 10], [4, 20]],
            [[1, 10], [3, 30], [4, 20]],
            [[2, 30], [4, 10]],
            [[0, 30], [1, 20], [2, 20], [3, 10]]
        ]
        self.num_nodes = 5

    def test_prim(self):
        cost = prim(self.edge, self.num_nodes)
        self.assertEqual(cost, 50)

    def test_kruskal(self):
        edge_list = []
        for i, v in enumerate(self.edge):
            for j, w in v:
                edge_list.append([i, j, w])
        cost = kruskal(edge_list, self.num_nodes)
        self.assertEqual(cost, 50)


if __name__ == "__main__":
    unittest.main()
