# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        curr_tree = False
        if not root.left and not root.right:
            curr_tree =  True
        elif not root.left:
            curr_tree = (root.val < root.right.val)
        elif not root.right:
            curr_tree = (root.val > root.left.val)
        else:
            curr_tree = (root.val < root.right.val) and (root.val > root.left.val)

        return curr_tree and self.isValidBST(root.left) and self.isValidBST(root.right)
        

            

            
        