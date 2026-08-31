# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.diameterHelper(root)
        return self.max_length
        
    def diameterHelper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.diameterHelper(node.left)
        right = self.diameterHelper(node.right)

        # Longest path through the current node in terms of edges
        self.max_length = max(self.max_length, left + right)

        # Return height of this subtree to the parent
        return 1 + max(left, right)