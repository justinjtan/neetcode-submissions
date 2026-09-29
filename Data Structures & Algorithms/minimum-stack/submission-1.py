class MinStack:

    def __init__(self):
        self.uid = 0
        self.stack = []
        self.min_heap = []
        self.stale_uid = set()

    def push(self, val: int) -> None:
        self.stack.append((val, self.uid))
        heapq.heappush(self.min_heap, (val, self.uid))
        self.uid += 1

    def pop(self) -> None:
        _, uid = self.stack.pop()
        self.stale_uid.add(uid)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        while self.min_heap and self.min_heap[0][1] in self.stale_uid:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
