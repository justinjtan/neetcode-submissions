class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)
        for idx in range(0, len(nums)):
            if target - nums[idx] in hashMap:
                return [hashMap[target - nums[idx]], idx]
            else:
                hashMap[nums[idx]] = idx
        return hashMap
        #WCRT: O(N) | Space: O(N)