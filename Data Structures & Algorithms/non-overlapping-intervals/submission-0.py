class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur = intervals[0]

        for i in range(1, len(intervals)):
            if cur[1] > intervals[i][0]:
                res += 1
                cur = [max(intervals[i][0], cur[0]), min(intervals[i][1], cur[1])]
            else:
                cur = intervals[i]
        
        return res
        #WCRT: O(N log N) | Space: O(1)