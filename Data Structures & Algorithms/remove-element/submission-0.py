class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        idx_to_delete = []
        idx_offset = 0
        for i in range(len(nums)):
            if nums[i] == val:
                idx_to_delete.append(i)
        
        for idx in idx_to_delete:
            nums.pop(idx - idx_offset)
            idx_offset += 1
        
        return n - len(idx_to_delete)