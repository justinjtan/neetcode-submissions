class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        cur = x
        cur_pow = 1
        tmp = n
        n = abs(n)
        while n != 0:
            while True:
                if cur_pow * 2 > n:
                    break
                cur *= cur
                cur_pow *= 2
            n -= cur_pow
            res *= cur
            cur = x
            cur_pow = 1
        
        if tmp < 0:
            return 1 / res
        return res
        #WCRT: O(log N) | Space: O(1)