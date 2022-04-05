from src import lc_subsequence, lc_substring
import unittest


class TestString(unittest.TestCase):
    def test_lc_subsequence(self):
        self.assertEqual(lc_subsequence("aaabbbc", "xaacx"), "aac")
        self.assertEqual(lc_subsequence("tokyo", "kyoto"), "kyo")

    def test_lc_substring(self):
        self.assertEqual(lc_substring("aaabbbc", "xaacx"), "aa")
        self.assertEqual(lc_substring("tokyo", "kyoto"), "kyo")


if __name__ == "__main__":
    unittest.main()
