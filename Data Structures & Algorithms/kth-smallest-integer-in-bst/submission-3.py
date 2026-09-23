# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = []
        def inorder(node, l1):
            if node is None:
                return
            inorder(node.left, l1)
            l1.append(node.val)
            inorder(node.right, l1)
        inorder(root, ans)
        return ans[k - 1]
