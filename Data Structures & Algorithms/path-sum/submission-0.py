# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, total):
            if not node:
                return False

            total += node.val

            if not node.left and not node.right and total != targetSum:
                return False
            
            if not node.left and not node.right and total == targetSum:
                return True
            
            
            return helper(node.left, total) or helper(node.right, total)

        return helper(root, 0)

        