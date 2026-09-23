# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #can just take the path of both and 

        cur = root
        while cur:
            if cur.val <= max(p.val, q.val) and cur.val >= min(p.val, q.val):
                return cur
            if cur.val >= max(p.val, q.val):
                cur = cur.left
            else:
                cur = cur.right

            

        
