# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    res += "n"
                    continue
                res += "#"
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res
        #WCRT: O(N) | Space: O(N)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        root_val = ""
        data_idx = -1
        for idx in range(1, len(data)):
            if data[idx] == "#" or data[idx] == "n":
                data_idx = idx
                break
            root_val += data[idx]
        root = TreeNode(int(root_val))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left_val = ""
            right_val = ""
            is_start = False
            for i in range(2):
                while not is_start or data[data_idx] != "#":
                    if data[data_idx] == "n":
                        if i == 0:
                            if left_val == "":
                                left_val = "n"
                                data_idx += 1
                        elif i == 1:
                            if right_val == "":
                                right_val = "n"
                                data_idx += 1
                        break
                    if data[data_idx] == "#":
                        is_start = True
                        data_idx += 1
                        continue
                    if i == 0:
                        left_val += data[data_idx]
                    else:
                        right_val += data[data_idx]
                    data_idx += 1
                is_start = False
            if left_val != "n":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                queue.append(left_node)
            if right_val != "n":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                queue.append(right_node)
            
        return root
        #WCRT: O(N) | Space: O(N)
