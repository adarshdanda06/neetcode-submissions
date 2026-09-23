# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        cur = root
        #either needs to be greater than both or less than both
        cond1 = (cur.val > p.val and cur.val > q.val)
        cond2 = (cur.val < p.val and cur.val < q.val)
        while ((cond1 or cond2) and cur is not None):
            if cond1:
                cur = cur.left
            elif cond2:
                cur = cur.right
            ans = cur
            cond1 = (cur.val > p.val and cur.val > q.val)
            cond2 = (cur.val < p.val and cur.val < q.val)
        return ans
    



        
