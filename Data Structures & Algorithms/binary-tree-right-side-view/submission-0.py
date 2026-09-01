# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # always add the right most side
        # each level we will add 1
        res = []

        def helper(node, level):
            if not node:
                return

            # the spot is already taken
            if len(res) < level + 1:
                res.append(node.val)

            helper(node.right, level + 1)
            helper(node.left, level + 1)

        helper(root, 0)
        return res
        