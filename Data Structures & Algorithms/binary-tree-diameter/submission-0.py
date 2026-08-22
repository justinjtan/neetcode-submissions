# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def _helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self._helper(root.left)
        right = self._helper(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0
        x =self._helper(root)
        return self.res
        #WCRT: O(N) | Space: O(N)
    