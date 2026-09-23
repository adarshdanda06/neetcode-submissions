# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, less, great):
            if (root is None): 
                return True
            if not (less < root.val < great):
                return False

        #store like some_min or max
            if (root.left is not None and root.val <= root.left.val):
                return False
            if (root.right is not None and root.val >= root.right.val):
                return False
    
            return helper(root.right, root.val, great) and helper(root.left, less, root.val) 
        return helper(root, float('-inf'), float('inf'))
            
        
        

        
        