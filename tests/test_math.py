from src import gcd, lcm, is_prime, eratosthenes_sieve, divisor, prime_decomposition
import unittest


class TestMath(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(32, 48), 16)

    def test_lcm(self):
        self.assertEqual(lcm(32, 48), 96)

    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(4), False)

    def test_eratosthenes_sieve(self):
        n = 12
        ans = [False, False, True, True, False, True, False, True, False, False, False, True, False]
        self.assertEqual(eratosthenes_sieve(n), ans)

    def test_divisor(self):
        n = 12
        ans = [1, 2, 3, 4, 6, 12]
        self.assertEqual(divisor(n), ans)

    def test_prime_decomposition(self):
        n = 12
        ans = [2, 2, 3]
        self.assertEqual(prime_decomposition(n), ans)


if __name__ == "__main__":
    unittest.main()
