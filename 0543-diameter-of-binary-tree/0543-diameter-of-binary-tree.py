# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def find_height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            nonlocal max_diameter
            left_height = find_height(root.left)
            right_height = find_height(root.right)

            # update max_diameter
            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        find_height(root)
        return max_diameter
