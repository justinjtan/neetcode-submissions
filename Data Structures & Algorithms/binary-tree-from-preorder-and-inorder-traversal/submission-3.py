# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: idx for idx, val in enumerate(inorder)}
        idx = 0

        def dfs(lo, hi):
            nonlocal idx
            if lo > hi:
                return None
            node = TreeNode(preorder[idx])
            idx += 1
            mid = pos[node.val]
            node.left = dfs(lo, mid - 1)
            node.right = dfs(mid + 1, hi)
            return node
        
        return dfs(0, len(preorder) - 1)
        #WCRT: O(N) | Space: O(N)
