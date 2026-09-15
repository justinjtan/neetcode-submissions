class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > cur[1] or intervals[i][1] < cur[0]:
                res.append(cur)
                cur = intervals[i]
            else:
                cur = [min(intervals[i][0], cur[0]), max(intervals[i][1], cur[1])]
        
        if cur:
            res.append(cur)
        
        return res
        #WCRT: O(N Log N) | Space: O(1) extra space and O(N) for output space.