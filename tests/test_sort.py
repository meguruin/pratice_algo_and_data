from src import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort
import unittest


class TestSort(unittest.TestCase):
    def test_selection_sort(self):
        x = [8, 1, 4, 2, 3, 9, 3, -1]
        sorted_x = [-1, 1, 2, 3, 3, 4, 8, 9]
        self.assertEqual(selection_sort(x), sorted_x)

    def test_bubble_sort(self):
        x = [8, 1, 4, 2, 3, 9, 3, -1]
        sorted_x = [-1, 1, 2, 3, 3, 4, 8, 9]
        self.assertEqual(bubble_sort(x), sorted_x)

    def test_insertion_sort(self):
        x = [8, 1, 4, 2, 3, 9, 3, -1]
        sorted_x = [-1, 1, 2, 3, 3, 4, 8, 9]
        self.assertEqual(insertion_sort(x), sorted_x)

    def test_merge_sort(self):
        x = [8, 1, 4, 2, 3, 9, 3, -1]
        sorted_x = [-1, 1, 2, 3, 3, 4, 8, 9]
        self.assertEqual(merge_sort(x), sorted_x)

    def test_quick_sort(self):
        x = [8, 1, 4, 2, 3, 9, 3, -1]
        sorted_x = [-1, 1, 2, 3, 3, 4, 8, 9]
        self.assertEqual(quick_sort(x), sorted_x)


if __name__ == "__main__":
    unittest.main()
