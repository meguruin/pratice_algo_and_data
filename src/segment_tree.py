"""
    Segment Tree: get calculated value for [l, r)
    - This implementation uses not-recursion algorithm
    - ref: https://qiita.com/dn6049949/items/afa12d5d079f518de368
    Time complexity:  O(log(n)) (both update and query)
    Space complexity: O(2**n)
"""


class SegmentTree:
    def __init__(self, n, f, e):
        self.n = (2 ** n - 1).bit_length()
        self.f = f
        self.e = e
        self.mem = [self.e for i in range(self.n * 2)]

    def update(self, i, v):
        i += self.n
        self.mem[i] = v
        while i > 0:
            i //= 2
            l_child = i * 2
            r_child = i * 2 + 1
            self.mem[i] = self.f(self.mem[l_child], self.mem[r_child])

    def query(self, l, r):
        l += self.n
        r += self.n
        lres, rres = self.e, self.e
        while l < r:
            if l & 1:
                lres = self.f(lres, self.mem[l])
                l += 1
            if r & 1:
                rres = self.f(rres, self.mem[r - 1])
                r -= 1
            l //= 2
            r //= 2
        return self.f(lres, rres)
