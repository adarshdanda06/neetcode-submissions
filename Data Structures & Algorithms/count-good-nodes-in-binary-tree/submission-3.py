# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, curr_max):
            nonlocal count
            curr_max = max(root.val, curr_max)
            if root.val >= curr_max:
                count += 1

            if not root.left and not root.right:
                return 

            if root.left:
                l = dfs(root.left, curr_max)

            if root.right:
                r = dfs(root.right, curr_max)

        dfs(root, -100)
        return count
            
            