# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def dfs(root, p, q):
            nonlocal res
            if not root:
                return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right:
                res = root
            elif root.val == p.val or root.val == q.val:
                if left or right:
                    res = root
                return True
            return left or right

        dfs(root, p, q)
        return res
        #WCRT: O(N) | Space: O(N)
