# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if abs(left - right) > 1:
                self.is_balanced = False
            
            return 1 + max(left, right)

        helper(root)
        return self.is_balanced
        