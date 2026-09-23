# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        q.append(root)
        
        lvl = 0
        while q:
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node:
                    if lvl > len(res) - 1:
                        res.append(node.val)
                    else:
                        res[lvl] = node.val
                    q.append(node.left)
                    q.append(node.right)
            lvl += 1
        
        return res