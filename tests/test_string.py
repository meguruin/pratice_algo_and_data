from src import cls
import unittest


class TestString(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(cls("aaabbbc", "xaacx"), "aac")
        self.assertEqual(cls("tokyo", "kyoto"), "kyo")


if __name__ == "__main__":
    unittest.main()
