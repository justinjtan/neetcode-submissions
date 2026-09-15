class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_lower_idx = 0
        new_upper_idx = len(intervals) - 1

        for i in range(len(intervals)):
            lower_bound = intervals[i][0]
            upper_bound = intervals[i][1]
            if newInterval[0] > upper_bound:
                new_lower_idx = i + 1
        
        for i in range(len(intervals) - 1, -1, -1):
            lower_bound = intervals[i][0]
            upper_bound = intervals[i][1]
            if newInterval[1] < lower_bound:
                new_upper_idx = i - 1
        
        res = intervals[:new_lower_idx]
        print(new_lower_idx)
        print(new_upper_idx)
        if new_lower_idx > new_upper_idx:
            res.append(newInterval)
            res += intervals[new_upper_idx + 1:]
        else:
            res.append([min(intervals[new_lower_idx][0], newInterval[0]), max(intervals[new_upper_idx][1], newInterval[1])])
            res += intervals[new_upper_idx + 1:]
        
        return res
        #WCRT: O(N) | Space: O(1) extra space and O(N) for output space.