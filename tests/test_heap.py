from src import Heap
import unittest


class TestHeap(unittest.TestCase):
    def setUp(self):
        x = [0, 3, 1, 4, 10, 7]
        self.heap = Heap(x)

    def test_pop(self):
        x = self.heap.pop()
        self.assertEqual(x, 0)

    def test_push(self):
        self.heap.push(-1)
        x = self.heap.pop()
        self.assertEqual(x, -1)


if __name__ == "__main__":
    unittest.main()
