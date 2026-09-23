# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        #if any node on walk greater than destination, not a good node
        #if destination greatest, considered a good node
        def recurse(cur, max_val):
            if cur is None:
                return 0
            if max_val > cur.val:
                count = 0
            else:
                count = 1
            
            count += recurse(cur.left, max(cur.val, max_val))
            count += recurse(cur.right, max(cur.val, max_val))
            return count
        
        return recurse(root, root.val)
