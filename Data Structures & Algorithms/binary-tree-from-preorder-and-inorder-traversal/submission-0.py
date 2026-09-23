# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recurse(pre, ino):
            if (len(pre) == 0 or len(ino) == 0):
                return None
        
            root = TreeNode(pre[0])

            root_ind = ino.index(root.val)

            left_inorder = ino[:root_ind]
            right_inorder = ino[root_ind + 1:]


            left_pre = pre[1: 1 + len(left_inorder)]
            right_pre = pre[len(left_pre) + 1: ]

            root.left = recurse(left_pre, left_inorder)
            root.right = recurse(right_pre, right_inorder)

            return root
        
        return recurse(preorder, inorder)

        











        

        