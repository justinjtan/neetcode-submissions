import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_freq = defaultdict(int)

        for num in nums:
            nums_freq[num] += 1
            if nums_freq[num] > math.floor(len(nums) / 2):
                return num
        
        return -1