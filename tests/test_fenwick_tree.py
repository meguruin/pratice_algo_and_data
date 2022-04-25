from src import FenwickTree
import unittest


class TestFenwickTree(unittest.TestCase):
    def setUp(self):
        self.tree = FenwickTree(10)

    def test_fenwick_tree(self):
        self.assertEqual(self.tree.query(0, 10), 0)
        self.tree.update(0, 1)
        self.tree.update(1, 10)
        self.tree.update(3, 1000)
        self.assertEqual(self.tree.query(0, 10), 1011)
        self.assertEqual(self.tree.query(1, 2), 10)
        self.assertEqual(self.tree.query(0, 2), 11)


if __name__ == "__main__":
    unittest.main()
