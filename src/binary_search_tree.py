class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, nums):
        self.root = None
        for d in nums:
            self.insert(d)

    def insert(self, a):
        if self.root is None:
            self.root = Node(a)
        else:
            self._insert(self.root, Node(a))
        return True

    def _insert(self, root, a):
        if root.data < a.data:
            if root.right is None:
                root.right = a
            else:
                self._insert(root.right, a)
        else:
            if root.left is None:
                root.left = a
            else:
                self._insert(root.left, a)

    def max(self):
        if self.root is None:
            return None
        else:
            return self._max(self.root).data

    def _max(self, a):
        if a.right is None:
            return a
        else:
            return self._max(a.right)

    def min(self):
        if self.root is None:
            return None
        else:
            return self._min(self.root).data

    def _min(self, a):
        if a.left is None:
            return a
        else:
            return self._min(a.left)

    def search(self, v):
        if self.root is None:
            return None
        else:
            return self._search(self.root, v)

    def _search(self, node, v):
        if v == node.data:
            return True
        elif v < node.data:
            if node.left is None:
                return False
            return self._search(node.left, v)
        else:
            if node.right is None:
                return False
            return self._search(node.right, v)

    # 直接ポインタが扱えないので、子を返すような実装にする必要がある
    def remove(self, v):
        if self.root:
            self.root = self._remove(self.root, v)
        return False

    def _remove(self, node, v):
        if not node:
            return node
        if v < node.data:
            node.left = self._remove(node.left, v)
        elif v > node.data:
            node.right = self._remove(node.right, v)
        else:
            if not node.right and not node.left:
                del node
                return None
            if not node.right:
                tmp = node.left
                del node
                return tmp
            if not node.left:
                tmp = node.right
                del node
                return tmp
            tmp = self._max(node.left)
            node.data = tmp.data
            node.left = self._remove(node.left, tmp.data)
        return node

    def print_tree(self):
        if self.root is None:
            print("Empty")
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        left_v = -100 if node.left is None else node.left.data
        right_v = -100 if node.right is None else node.right.data
        print("data, left, right: ", node.data, left_v, right_v)
        if node.left is not None:
            self._print_tree(node.left)
        if node.right is not None:
            self._print_tree(node.right)
