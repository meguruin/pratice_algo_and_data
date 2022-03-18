#    0       ←0
#  1   3     ←1, 2
# 2 3 8 3    ←3, 4, 5, 6
class Heap:
    def __init__(self, nums):
        self.heap = []
        for num in nums:
            self.push(num)

    def pop(self):
        res = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) == 0:
            return res
        self.heap[0] = last
        self.heapify_down()
        return res

    def push(self, num):
        self.heap.append(num)
        self.heapify_up()

    # reorder self.heap from the tail
    def heapify_up(self):
        now = len(self.heap) - 1
        par = self._get_parent(now)
        while now >= 0 and par >= 0 and self.heap[now] < self.heap[par]:
            self.heap[now], self.heap[par] = self.heap[par], self.heap[now]
            now = par
            par = self._get_parent(now)

    def _get_parent(self, idx):
        return (idx - 1) // 2

    def _get_left_child(self, idx):
        return idx * 2 + 1

    def _get_right_child(self, idx):
        return idx * 2 + 2

    def heapify_down(self):
        now = 0
        left_child = self._get_left_child(now)
        right_child = self._get_right_child(now)
        while right_child < len(self.heap):
            if self.heap[now] > min(self.heap[left_child], self.heap[right_child]):
                if self.heap[left_child] < self.heap[right_child]:
                    self.heap[left_child], self.heap[now] = self.heap[now], self.heap[left_child]
                    now = left_child
                else:
                    self.heap[right_child], self.heap[now] = self.heap[now], self.heap[right_child]
                    now = right_child
            left_child = self._get_left_child(now)
            right_child = self._get_right_child(now)
