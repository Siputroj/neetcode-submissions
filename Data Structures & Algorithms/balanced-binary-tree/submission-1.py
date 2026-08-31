# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # faster solution using an array return

        def helper(node):
            if not node:
                return [True, 0]
                
            left, right = helper(node.left), helper(node.right)
            balanced = (abs(left[1] - right[1]) <= 1 and left[0] and right[0])

            return [balanced, 1 + max(left[1], right[1])]
        
        return helper(root)[0]