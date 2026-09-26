class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_freq = set()
        for num in nums:
            if num in nums_freq:
                return True
            nums_freq.add(num)
        return False