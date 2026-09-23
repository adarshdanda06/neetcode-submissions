# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def traverse(root, maxVal):
            if (root == None):
                return 0

            currBiggest = max(root.val, maxVal)
            if (root.val >= maxVal):
                return 1 + traverse(root.left, currBiggest) + traverse(root.right, currBiggest)

            return traverse(root.left, currBiggest) + traverse(root.right, currBiggest)


        return traverse(root, root.val) 
            