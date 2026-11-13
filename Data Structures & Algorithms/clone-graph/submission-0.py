"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

adjList = [[2, 3],[1,3],[1, 2]]
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # check following op with visited set
        if not node:
            return None
        visited = set()
        valToNode = {}
        complete = set()

        # [[2, 3],[1,3],[1, 2]]
        def dfs(node):
            if node.val in visited or node.val in complete:
                return valToNode[node.val] # copy node

            copyNode = None
            if node.val not in valToNode:
                copyNode = Node(node.val)
            else:
                copyNode = valToNode[node.val]

            valToNode[node.val] = copyNode
            visited.add(node.val)

            neighList = []
            for neighbor in node.neighbors:
                neighborNode = dfs(neighbor)
                neighList.append(neighborNode)

            complete.add(node.val)
            visited.remove(node.val)

            copyNode.neighbors = neighList
            # valToNode[node.val] = copyNode
            return copyNode

        return dfs(node)

        # if node isnt created:
            # create the node

        # dfs into neighbors if not prev
        # add to neighbors of node into curr adj list
            # 
        # 1: [2]