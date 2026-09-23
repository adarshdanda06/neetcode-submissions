# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            l = len(q)
            res.append(q[-1].val)
            for num in range(l):
                val = q.popleft()
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)

        return res