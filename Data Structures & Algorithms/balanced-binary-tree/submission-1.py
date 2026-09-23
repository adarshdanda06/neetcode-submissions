# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def depth(root):
            nonlocal balanced
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            l = depth(root.left) + 1
            r = depth(root.right) + 1

            if abs(l - r) > 1:
                balanced = False

            return max(l, r)
            
        depth(root)
        return balanced