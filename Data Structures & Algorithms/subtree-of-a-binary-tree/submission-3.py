# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        

        def search(baseRoot, subRoot):
            if not baseRoot and not subRoot:
                return True
            if not baseRoot or not subRoot:
                return False
            if baseRoot.val != subRoot.val:
                return False
            
            l = search(baseRoot.left, subRoot.left)
            r = search(baseRoot.right, subRoot.right)

            return l and r

        def dfs(root):
            if not root:
                return False

            if search(root, subRoot):
                return True

            l = dfs(root.left)
            r = dfs(root.right)

            return l or r

        return dfs(root)


            