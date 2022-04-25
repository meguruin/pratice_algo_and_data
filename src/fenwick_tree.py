"""
    Fenwick Tree(Binary Indexed Tree): get sum for [l, r)
        - ref: https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
    Time complexity:  O(log(n)) (both update and query)
    Space complexity: O(n)
"""


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.mem = [0 for i in range(self.n)]

    def update(self, i, v):
        i += 1
        while i < self.n:
            self.mem[i - 1] += v
            i += i & -i

    def query(self, l, r):
        assert 0 <= l <= r <= self.n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        res = 0
        while r > 0:
            res += self.mem[r - 1]
            r -= r & -r
        return res
