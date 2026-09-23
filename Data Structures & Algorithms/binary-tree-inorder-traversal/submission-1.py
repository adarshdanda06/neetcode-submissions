# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        visited = []
        stack = []

        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        
        while len(stack) > 0:
            top_elem = stack[-1]
            stack.pop()
            visited.append(top_elem.val)
            
            if top_elem.right:
                stack.append(top_elem.right)
                itera = top_elem.right
                while itera.left:
                    stack.append(itera.left)
                    itera = itera.left
            
        return visited

