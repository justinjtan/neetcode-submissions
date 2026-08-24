# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            curr = root.val
            curr += left if left > 0 else 0
            curr += right if right > 0 else 0
            res = max(res, curr)
            return root.val + max(left, right, 0)

        dfs(root)
        return res
        #WCRT: O(N) | Space: O(N)