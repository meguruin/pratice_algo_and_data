from src import lcs
import unittest


class TestString(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcs("aaabbbc", "xaacx"), "aac")
        self.assertEqual(lcs("tokyo", "kyoto"), "kyo")


if __name__ == "__main__":
    unittest.main()
