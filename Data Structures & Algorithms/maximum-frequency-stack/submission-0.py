class FreqStack:

    def __init__(self):
        self.max_heap = []
        self.nums = defaultdict(int)
        self.pq = 0

    def push(self, val: int) -> None:
        self.nums[val] += 1
        heapq.heappush(self.max_heap, (-self.nums[val], -self.pq, val))
        self.pq += 1
        #WCRT: O(log N)

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.max_heap)
        self.nums[val] -= 1
        return val
        #WCRT: O(log N)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()