# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqualTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root1, root2):
            nonlocal res
            if not(root1 or root2):
                return
            elif (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
                res = False
                return
            left = dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)
        
        dfs(root1, root2)
        return res

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_equal = False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and self.isEqualTree(node, subRoot):
                is_equal = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return is_equal
        #WCRT: O(N * M) | Space: O(N + M) where N is the number of edges in root and M is the number of edges in subRoot