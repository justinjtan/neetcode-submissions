class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        res = 0

        acc = 0
        for num in nums:
            acc += num
            res += 1 if acc == k else 0
            if acc - k in prefix_sum:
                res += prefix_sum[acc - k]
            prefix_sum[acc] += 1
        
        return res