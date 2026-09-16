class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        upper_bound = (2 ** 31) - 1
        lower_bound = -(2 ** 31)
        res = []
        for i in range(len(str_x) - 1, 0, -1):
            res.append(str_x[i])
        if x >= 0:
            res.append(str_x[0])
        res_str = "".join(res)
        if x < 0:
            return -int(res_str) if lower_bound <= -int(res_str) else 0
        return int(res_str) if upper_bound >= int(res_str) else 0
        #WCRT: O(N) | Space: O(N)