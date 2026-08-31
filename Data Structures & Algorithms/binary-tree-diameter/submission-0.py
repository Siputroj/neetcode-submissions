# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0  # Regular local variable

        def helper(node):
            nonlocal max_length  # Accesses outer function's variable
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            max_length = max(max_length, left + right)

            return 1 + max(left, right)

        helper(root)
        return max_length

        
            