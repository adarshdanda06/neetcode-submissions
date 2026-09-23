# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val
        #if along path, there is a node greater than destination, then not a good node
        #otherwise it is a good node
        def recurse(cur, max_val):
            if cur is None:
                return 0
            if max_val <= cur.val:
                ans = 1
            else:
                ans = 0
            ans += recurse(cur.left, max(cur.val, max_val))

            ans += recurse(cur.right, max(cur.val, max_val))
            return ans
        return recurse(root, root.val)