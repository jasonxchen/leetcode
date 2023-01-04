# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False

        if root.left:
            if not self.isBalanced(root.left):
                return False
        if root.right:
            if not self.isBalanced(root.right):
                return False
        
        return True

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        elif not node.left and not node.right:
            return 1
        
        left_depth, right_depth = 0, 0
        if node.left:
            left_depth = 1 + self.depth(node.left)
        if node.right:
            right_depth = 1 + self.depth(node.right)
            
        return max(left_depth, right_depth)
