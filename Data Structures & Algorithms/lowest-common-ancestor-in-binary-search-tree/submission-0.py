# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = None
        if p.val > q.val:
            p, q = q, p
        def search(root):
            nonlocal res
            if root.val == p.val or root.val == q.val or (p.val <= root.val and q.val >= root.val):
                res = root
                return
            if p.val < root.val and q.val < root.val:
                return search(root.left)
            if p.val > root.val and q.val > root.val:
                return search(root.right)

        search(root)
        return res