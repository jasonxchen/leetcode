# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        queue = []
        curr_node = root
        while curr_node.left or curr_node.right or queue:
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            curr_node = queue.pop(0)
        return root
