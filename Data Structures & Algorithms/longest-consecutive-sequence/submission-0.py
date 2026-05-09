class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1
        res = 0
        for num in nums:
            if hashMap.get(num, 0) == 0:
                continue
            hashMap[num] = 0 
            ct = 1
            smallest = num
            largest = num
            while hashMap.get(smallest - 1, 0) != 0 or hashMap.get(largest + 1, 0) != 0:
                if hashMap.get(smallest - 1, 0) != 0:
                    ct += 1
                    smallest -= 1
                    hashMap[smallest] = 0
                if hashMap.get(largest + 1, 0) != 0:
                    ct += 1
                    largest += 1
                    hashMap[largest] = 0
            if ct > res:
                res = ct
        return res
        #WCRT: O(N) | Space: O(N)