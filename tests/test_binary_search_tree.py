from src import BinarySearchTree
import unittest


class TestBibarySearchTree(unittest.TestCase):
    def setUp(self):
        x = [3, 1, 3, 5, 2]
        self.bst = BinarySearchTree(x)

    def test_max(self):
        expected = 5
        actual = self.bst.max()
        self.assertEqual(expected, actual)

    def test_min(self):
        expected = 1
        actual = self.bst.min()
        self.assertEqual(expected, actual)

    def test_search_exists(self):
        expected = True
        actual = self.bst.search(3)
        self.assertEqual(expected, actual)

    def test_search_no_exists(self):
        expected = False
        actual = self.bst.search(4)
        self.assertEqual(expected, actual)

    def test_insert(self):
        self.bst.insert(0)
        expected = 0
        actual = self.bst.min()
        self.assertEqual(expected, actual)

    def test_remove(self):
        self.bst.remove(5)
        expected = 3
        actual = self.bst.max()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
