# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node, maxVal):
            if not node:
                return

            if maxVal <= node.val:
                self.res += 1
                helper(node.left, node.val)
                helper(node.right, node.val)
            else:
                helper(node.left, maxVal)
                helper(node.right, maxVal)

        helper(root, -101)
        return self.res


        
        