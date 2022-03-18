class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.siz = [1 for i in range(n)]
        self.n = n

    def root(self, a):
        while a != self.par[a]:
            a = self.par[a]
        return a

    def issame(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        if self.siz[a] < self.siz[b]:
            a, b = b, a
        self.siz[a] += self.siz[b]
        self.par[b] = self.par[a]
        return

    def size(self, a):
        return self.siz[self.root(a)]

    def check_index(self, a):
        if a < 0 or a > self.n:
            print("Error index")
            return False
        return True
