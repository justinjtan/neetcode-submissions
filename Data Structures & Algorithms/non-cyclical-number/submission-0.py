class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        str_n = str(n)

        while str_n not in visited and str_n != '1':
            visited.add(str_n)
            res = 0
            for num in str_n:
                res += int(num) ** 2
            str_n = str(res)
        
        return str_n == '1'
        #WCRT: O(N) | Space: O(N)