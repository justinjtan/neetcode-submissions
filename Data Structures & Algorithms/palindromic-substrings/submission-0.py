class Solution:
    def countSubstrings(self, s: str) -> int:
        res, n = 0, len(s)
        for i in range(n):
            #odd length palindrome case
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                res += 1
            
            #even length palindrome case
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                res += 1
        return res
        #WCRT: O(N^2) | Space: O(1)