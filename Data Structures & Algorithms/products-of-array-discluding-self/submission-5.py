class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            prefix_products[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix_products[i] = product
            product *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix_products[i] * suffix_products[i])
        
        return res