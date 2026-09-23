# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        res = 0

        def dfs(root):
            nonlocal res
            nonlocal count
            if not root:
                return
            l = dfs(root.left)
            count += 1
            if count == k:
                res = root.val
            r = dfs(root.right)

            return

        dfs(root)
        return res


        dfs(root)
        return res