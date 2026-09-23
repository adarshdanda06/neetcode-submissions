# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # somehow keep track of min and max
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_val, max_val):
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            l = dfs(root.left, min_val, root.val)
            r = dfs(root.right, root.val, max_val)

            return l and r





        return dfs(root, -1001, 1001)

            