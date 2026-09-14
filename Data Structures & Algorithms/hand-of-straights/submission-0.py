class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        min_val = float("inf")
        max_val = float("-inf")
        hand_freq = defaultdict(int)

        for val in hand:
            hand_freq[val] += 1
            min_val = min(min_val, val)
            max_val = max(max_val, val)

        for i in range(min_val, max_val + 1):
            if hand_freq.get(i, False):
                min_val_freq = hand_freq[i]
                for j in range(groupSize):
                    if hand_freq.get(i + j, 0) - min_val_freq < 0:
                        return False
                    hand_freq[i + j] -= min_val_freq

        return True
        #WCRT: O(N) | Space: O(N)