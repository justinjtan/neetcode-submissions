import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums_freq = Counter(nums)

        for num, ct in nums_freq.items():
            if ct > math.floor(len(nums) / 3):
                res.append(num)
        
        return res