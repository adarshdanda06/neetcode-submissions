# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(cur, lower, upper):
            if cur is None:
                return True
            
            if (cur.val <= lower or cur.val >= upper):
                return False
            
            return helper(cur.right, cur.val, upper)  and helper(cur.left, lower, cur.val)

        return helper(root, float('-inf'), float('inf'))
        
        

        
        