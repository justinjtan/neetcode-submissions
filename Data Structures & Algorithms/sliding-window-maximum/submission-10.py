class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            if r - l + 1 == k:
                while l > max_heap[0][1]:
                    heapq.heappop(max_heap)
                max_num = max_heap[0][0]
                res.append(-max_num)
                l += 1
        
        return res
        #WCRT: O(N log K) | Space: O(K) extra space and O(N - K) for output space.