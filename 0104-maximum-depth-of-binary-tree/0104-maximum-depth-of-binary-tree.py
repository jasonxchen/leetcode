# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = []
        curr_node = (root, 1)
        level = 1
        while curr_node[0]:
            if curr_node[1] > level:
                level = curr_node[1]
            if curr_node[0].left:
                queue.append((curr_node[0].left, level + 1))
            if curr_node[0].right:
                queue.append((curr_node[0].right, level + 1))
            if queue:
                curr_node = queue.pop(0)
            else:
                return level
