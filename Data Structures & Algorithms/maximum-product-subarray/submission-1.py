class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sub_nums = []
        curr = []
        contains_zero = False
        for num in nums:
            if num == 0:
                contains_zero = True
                if curr:
                    sub_nums.append(curr)
                    curr = []
                continue
            curr.append(num)
        
        if curr:
            sub_nums.append(curr)

        res = 0 if contains_zero else float("-inf")
        for sub in sub_nums:
            total = 1
            for num in sub:
                total *= num
            if total > 0 or len(sub) == 1:
                res = max(res, total)
            else:
                temp = total
                for num in sub:
                    if temp > 0:
                        break
                    temp //= num
                res = max(res, temp)
                temp = total
                for i in range(len(sub) - 1, -1, -1):
                    if temp > 0:
                        break
                    temp //= sub[i]
                res = max(res, temp)
        return res
        #WCRT: O(N) | Space: O(N)