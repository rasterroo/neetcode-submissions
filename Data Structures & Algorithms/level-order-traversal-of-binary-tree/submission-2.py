# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we do bfs for each level
        if not root:
            return []

        queue = []
        result = []
        queue.append(root)

        while queue: 
            level_len = len(queue)
            level = []
            for i in range(level_len):
                node = queue.pop(0)
                if node is not None:
                    level.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

            result.append(level)

        return result 
            
