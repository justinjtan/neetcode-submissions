import math

class Solution:
    def deleteFromMaxHeap(self, interval: Tuple[int, int], max_heap: List[int]) -> None:   
        l, r = interval
        while l > max_heap[0][1]:
            max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
            max_heap.pop()
            curr_idx = 0
            left_child_idx = 2*curr_idx + 1
            right_child_idx = 2*curr_idx + 2
            if left_child_idx >= len(max_heap):
                break
            if right_child_idx >= len(max_heap):
                right_child_idx = left_child_idx
            while max_heap[curr_idx][0] < max_heap[left_child_idx][0] or max_heap[curr_idx][0] < max_heap[right_child_idx][0]:
                if max_heap[left_child_idx][0] >= max_heap[right_child_idx][0]:
                    max_heap[curr_idx], max_heap[left_child_idx] = max_heap[left_child_idx], max_heap[curr_idx]
                    curr_idx = left_child_idx
                else:
                    max_heap[curr_idx], max_heap[right_child_idx] = max_heap[right_child_idx], max_heap[curr_idx]
                    curr_idx = right_child_idx
                left_child_idx = 2*curr_idx + 1
                right_child_idx = 2*curr_idx + 2
                if left_child_idx >= len(max_heap):
                    break
                if right_child_idx >= len(max_heap):
                    right_child_idx = left_child_idx
        #WCRT: O(N log k)

    def insertToMaxHeap(self, num: int, idx: int, max_heap: List[int]) -> None:
        max_heap.append((num, idx))
        curr_idx = len(max_heap) - 1
        parent_idx = math.floor((curr_idx - 1) / 2)
        while curr_idx != 0 and max_heap[parent_idx][0] <= max_heap[curr_idx][0]:
            max_heap[parent_idx], max_heap[curr_idx] = max_heap[curr_idx], max_heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = math.floor((curr_idx - 1) / 2)
        #WCRT: O(log k)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        l = 0
        for r in range(len(nums)):
            self.insertToMaxHeap(nums[r], r, max_heap)
            if r >= k:
                l += 1
                self.deleteFromMaxHeap((l, r), max_heap)
            if r >= k - 1:
                res.append(max_heap[0][0])
        return res
        #WCRT: O(N log k) | Space: O(k)
                