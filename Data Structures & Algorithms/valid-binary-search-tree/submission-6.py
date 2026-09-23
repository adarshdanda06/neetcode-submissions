# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # somehow keep track of min and max
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(root, low, high):
            if not root:
                return True
            if root.left == None and root.right == None:
                return True
            l, r = True, True
            if root.left:                    
                if root.left.val < root.val and root.left.val > low:
                    l = dfs(root.left, low, root.val)
                else:
                    l = False
            if root.right:
                if root.right.val > root.val and root.right.val < high:
                    r = dfs(root.right, root.val, high)
                else:
                    r = False
                    
            return l and r
        return dfs(root, -1001, 1001)
