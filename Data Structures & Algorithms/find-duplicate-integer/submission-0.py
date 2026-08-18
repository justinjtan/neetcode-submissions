class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
            if num_map[num] > 1:
                return num
        