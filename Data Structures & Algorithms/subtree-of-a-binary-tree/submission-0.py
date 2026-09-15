# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(root, subroot):
            if not root and not subroot:
                return True
            elif not root or not subroot:
                return False

            if root.val != subroot.val:
                return helper(root.left, subroot) or helper(root.right, subroot)
            
            return root.val == subroot.val and helper(root.left, subroot.left) and helper(root.right, subroot.right)

            
        return helper(root, subRoot)

            





        # run issubroot on all

        