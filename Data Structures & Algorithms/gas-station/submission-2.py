class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res_idx = -1
        found_start = False
        cur = 0
        cur_positive = 0 #from res_idx afterwards
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if found_start:
                cur_positive += gas[i] - cost[i]
                if cur_positive < 0:
                    cur_positive = 0
                    res_idx = -1
                    found_start = False
            if not found_start and gas[i] - cost[i] >= 0:
                res_idx = i
                cur_positive += gas[i] - cost[i]
                found_start = True
        
        if cur < 0:
            return -1
        return res_idx
        #WCRT: O(N) | Space: O(1)