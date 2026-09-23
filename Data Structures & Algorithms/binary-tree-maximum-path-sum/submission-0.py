# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPathWeight = float('-inf')

        if (not root.left and not root.right):
            return root.val

        def dfs(root):
            nonlocal maxPathWeight
            if not root.left and not root.right:
                return root.val
            
            leftSubtreePathSum = float('-inf')
            if root.left:
                leftSubtreePathSum = max(dfs(root.left), leftSubtreePathSum)

            rightSubtreePathSum = float('-inf')
            if root.right:
                rightSubtreePathSum = max(dfs(root.right), rightSubtreePathSum)

            maxPathWeight = max(leftSubtreePathSum, rightSubtreePathSum, root.val,
                                leftSubtreePathSum + root.val, rightSubtreePathSum + root.val,
                                leftSubtreePathSum + root.val + rightSubtreePathSum, maxPathWeight)

            returnPath = max(leftSubtreePathSum + root.val, rightSubtreePathSum + root.val, root.val)
            return returnPath

        dfs(root)
        return maxPathWeight