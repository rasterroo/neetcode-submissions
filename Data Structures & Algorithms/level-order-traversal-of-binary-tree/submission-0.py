# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        
        queue = deque()
        queue.append((root, 0))
        hmap = defaultdict(list)

        while queue:
            node = queue.popleft()
            hmap[node[1]].append(node[0].val)
            if node[0].left:
                queue.append((node[0].left, node[1]+1))
            if node[0].right:
                queue.append((node[0].right, node[1]+1))

        for depth, nodes in dict(sorted(hmap.items(), key=lambda x:x[0])).items():
            result.append(nodes)
        return result
