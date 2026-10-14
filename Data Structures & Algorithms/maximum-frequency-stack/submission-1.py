class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list)
        self.nums = defaultdict(int)
        self.max_freq = 0
        #Space: O(N)

    def push(self, val: int) -> None:
        self.nums[val] += 1
        self.stacks[self.nums[val]].append(val)
        self.max_freq = max(self.max_freq, self.nums[val])
        #WCRT: O(1)

    def pop(self) -> int:
        while not self.stacks[self.max_freq] and self.max_freq > 0:
            self.max_freq -= 1
        if self.max_freq > 0:
            num = self.stacks[self.max_freq].pop()
            self.nums[num] -= 1
            return num
        return -1
        #WCRT: O(1)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()