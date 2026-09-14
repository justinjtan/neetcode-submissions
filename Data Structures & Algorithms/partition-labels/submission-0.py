class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        res = []
        for i in range(len(s)):
            last_idx[s[i]] = i

        breakpoint_idx = 0
        ct = 0

        for i in range(len(s)):
            ct += 1
            breakpoint_idx = max(breakpoint_idx, last_idx[s[i]])
            if i == breakpoint_idx:
                res.append(ct)
                ct = 0
        
        return res
        #WCRT: O(N) | Space: O(M) where N is length of s and M is number of unique characters.