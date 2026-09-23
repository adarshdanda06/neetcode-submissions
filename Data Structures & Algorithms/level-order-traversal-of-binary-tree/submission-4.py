# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:



        hash_map = defaultdict(list)
        ans = []
        if root is None:
            return ans
        
        queue = deque()
        visited = set()
        queue.append((root, 0))
        height = 0
        hash_map[height].append(root.val)
        while queue:
            cur, cur_height = queue.popleft()
            if cur.left and cur.left not in visited:
                hash_map[cur_height + 1].append(cur.left.val)
                visited.add(cur.left)
                queue.append((cur.left, cur_height + 1))
            
            if cur.right and cur.right not in visited:
                hash_map[cur_height + 1].append(cur.right.val)
                visited.add(cur.right)
                queue.append((cur.right, cur_height + 1))
        
        for i in hash_map:
            ans.append(hash_map[i])
        return ans


        
            

        