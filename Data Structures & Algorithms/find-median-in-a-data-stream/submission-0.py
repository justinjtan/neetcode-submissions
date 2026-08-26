class MedianFinder:

    def __init__(self):
        self.lo = [] #max heap
        self.hi = [] #min heap
        #Space: O(N)

    def addNum(self, num: int) -> None:
        if not self.lo and not self.hi:
            heapq.heappush(self.lo, -num)
        elif num >= -self.lo[0]:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -num)
        if len(self.lo) - len(self.hi) > 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) - len(self.lo) > 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        #WCRT: O(log n) 

    def findMedian(self) -> float:
        #what we need is lo_max_heap and hi_min_heap
        if len(self.lo) == len(self.hi):
            med_lo = -self.lo[0]
            med_hi = self.hi[0]
            return (med_lo + med_hi) / 2.0
        res = -self.lo[0] if len(self.lo) > len(self.hi) else self.hi[0]
        return res
        #WCRT: O(1)