class Solution:
    def reverseBits(self, n: int) -> int:
        res = n & 1
        n >>= 1
        ct = 1
        while n != 0:
            res <<= 1
            res |= 1 if n & 1 else 0
            n >>= 1
            ct += 1
        return res << (32 - ct)
        #WCRT: O(1) | Space: O(1)