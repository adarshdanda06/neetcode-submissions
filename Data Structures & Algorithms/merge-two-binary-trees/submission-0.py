# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        root1Val = 0 if not root1 else root1.val
        root2Val = 0 if not root2 else root2.val
        currNode = TreeNode(root1Val + root2Val)

        r1Left = None if not root1 else root1.left
        r2Left = None if not root2 else root2.left
        leftNode = self.mergeTrees(r1Left, r2Left)

        r1Right = None if not root1 else root1.right
        r2Right = None if not root2 else root2.right
        rightNode = self.mergeTrees(r1Right, r2Right)
        
        currNode.right = rightNode
        currNode.left = leftNode

        return currNode