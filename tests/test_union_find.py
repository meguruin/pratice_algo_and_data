from src import UnionFind
import unittest


class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(8)
        for i in [(1, 2), (2, 3), (1, 1), (7, 1), (5, 6)]:
            self.uf.unite(i[0], i[1])

    def test_issame_ok(self):
        self.assertEqual(self.uf.issame(1, 3), True)

    def test_issame_ng(self):
        self.assertEqual(self.uf.issame(7, 6), False)


if __name__ == "__main__":
    unittest.main()
