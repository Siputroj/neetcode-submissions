# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[]]
        def helper(node, level):
            if not node:
                return
            
            if len(res) < level + 1:
                res.append([node.val])
            else:
                res[level].append(node.val)

            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)

        return res
            
        

            