# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first_ptr = last_ptr = None
        prev = TreeNode(float("-inf"))
        
        def dfs(node):
            nonlocal first_ptr, last_ptr, prev
            if not node:
                return
            dfs(node.left)
            if node.val < prev.val:
                if not first_ptr:
                    first_ptr = prev
                last_ptr = node
            prev = node
            dfs(node.right)
        
        curr = root
        dfs(curr)
        first_ptr.val, last_ptr.val = last_ptr.val, first_ptr.val
        #WCRT: O(V + E) | Space: O(1)