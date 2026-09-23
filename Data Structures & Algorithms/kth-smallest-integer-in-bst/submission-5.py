# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = []
        def recurse(cur):
            if cur is None:
                return 
            recurse(cur.left)
            ordered_list.append(cur.val)
            recurse(cur.right)

        recurse(root)

        return ordered_list[k - 1]
        