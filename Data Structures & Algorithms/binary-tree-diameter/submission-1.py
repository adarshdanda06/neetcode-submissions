# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tot = 0

        def depth(root):
            nonlocal tot
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            l = depth(root.left) + 1
            r = depth(root.right) + 1

            tot = max(tot, l + r - 2)

            return max(l, r)
        
        depth(root)
        return tot