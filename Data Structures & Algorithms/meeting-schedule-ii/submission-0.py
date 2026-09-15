"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()
        s, e = 0, 0
        res = 0
        ct = 0
        while s < len(start):
            if start[s] < end[e]:
                ct += 1
                s += 1
                res = max(res, ct)
            else:
                e += 1
                ct -= 1
        
        return res
        #WCRT: O(N) | Space: O(N)