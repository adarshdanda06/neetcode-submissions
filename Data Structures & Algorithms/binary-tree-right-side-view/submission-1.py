# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [-1] * 100

        def recurse(head, level):
            if (not head):
                return None
            
            res[level] = head.val

            left = recurse(head.left, level + 1)
            right = recurse(head.right, level + 1)
        
        recurse(root, 0)
        ind = 0
        for i, num in enumerate(res):
            if num == -1:
                ind = i
                break
    
        return res[0: ind]
