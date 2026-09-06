class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        min_idx = nums.index(min(nums))
        print(min_idx)
        curr = 0
        prev_2, prev_1 = 0, 0
        uses_first = False
        uses_last = False
        for i in range(len(nums) -1):
            val = nums[(min_idx + + 1 + i) % len(nums)] + prev_2
            if val > prev_1:
                curr = val
                if i == len(nums) -2:
                    uses_last = True
            else:
                curr = prev_1
            prev_2 = prev_1
            prev_1 = curr
        prev_2, prev_1 = 0, 0
        for i in range(len(nums) -1):
            val = nums[(min_idx - 1 - i)] + prev_2
            if val > prev_1:
                curr = val
                if i == len(nums) -2:
                    uses_first = True
            else:
                curr = prev_1
            prev_2 = prev_1
            prev_1 = curr
        if not uses_first and not uses_last:
            curr += nums[min_idx]
        print(uses_first)
        print(uses_last)
        return curr
