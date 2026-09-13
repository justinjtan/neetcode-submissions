class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([0])
        level = 0
        visited = set()
        visited.add(0)
        while queue:
            for i in range(len(queue)):
                idx = queue.popleft()
                if idx == len(nums) - 1:
                    return level
                for j in range(1, nums[idx] + 1):
                    new_idx = idx + j
                    if new_idx not in visited:
                        visited.add(new_idx)
                        queue.append(new_idx)
            level += 1
        return -1
        #WCRT: O(N * M) | Space: O(N * M) where N is length of nums and M is sum(nums)