# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def find_height(root: TreeNode) -> int:
            if not root:
                return -1

            nonlocal max_diameter
            left_height = find_height(root.left)
            right_height = find_height(root.right)
            diameter = left_height + right_height + 2

            # update max_diameter
            if diameter > max_diameter:
                max_diameter = diameter

            return 1 + max(left_height, right_height)

        find_height(root)
        return max_diameter
