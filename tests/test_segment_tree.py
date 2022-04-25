from src import SegmentTree
import unittest


class TestHeap(unittest.TestCase):
    def setUp(self):
        testset1 = {"n": 8, "f": lambda x, y: x + y, "e": 0, "first_array": [i + 1 for i in range(8)]}
        testset2 = {"n": 12, "f": lambda x, y: min(x, y), "e": 2 ** 31 - 1, "first_array": [i + 1 for i in range(12)]}
        self.tree1 = SegmentTree(testset1["n"], testset1["f"], testset1["e"])
        for i, v in enumerate(testset1["first_array"]):
            self.tree1.update(i, v)
        self.tree2 = SegmentTree(testset2["n"], testset2["f"], testset2["e"])
        for i, v in enumerate(testset2["first_array"]):
            self.tree2.update(i, v)

    def test_query(self):
        self.assertEqual(self.tree1.query(1, 3), 5)
        self.assertEqual(self.tree1.query(7, 8), 8)
        self.assertEqual(self.tree2.query(4, 6), 5)
        self.assertEqual(self.tree2.query(1, 8), 2)

    def test_update(self):
        self.tree1.update(2, 100)
        self.assertEqual(self.tree1.query(1, 3), 102)
        self.tree2.update(2, 100)
        self.assertEqual(self.tree2.query(1, 8), 2)


if __name__ == "__main__":
    unittest.main()
