# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #on each level, essentially add the right most node and return that
        queue = deque()
        ans = []
        if root is None:
            return []
        queue.append(root)

        while len(queue) > 0:
            sm = []
            cur_length = len(queue)
            for i in range(cur_length):
                cur = queue.popleft()
                sm.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            ans.append(sm[-1])
        return ans


