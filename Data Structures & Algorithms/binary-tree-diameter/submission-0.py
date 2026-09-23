# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tot = 0
        
        def dfs(root):
            nonlocal tot
            if not root:
                return 0
            if root.left == None and root.right == None:
                return 1
            l = dfs(root.left)
            r = dfs(root.right)
            tot = max(tot, l + r)
            return max(l, r) + 1
        dfs(root)
        
        return tot