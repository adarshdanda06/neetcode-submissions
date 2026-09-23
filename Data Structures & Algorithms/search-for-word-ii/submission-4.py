class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False

    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.complete = True
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        res = set()
        MCOLS, MROWS = len(board[0]), len(board)
        def search(i, j, root, visited, curr):
            if i < 0 or i >= MROWS or j < 0 or j >= MCOLS or (i, j) in visited or not root or board[i][j] not in root.children:
                return 

            l = board[i][j]
            if l not in root.children:
                return

            visited.add((i, j))
            curr += l
            node = root.children[l]
            if node.complete:
                res.add(curr)
            
            search(i, j + 1, node, visited, curr)
            search(i, j - 1, node, visited, curr)
            search(i + 1, j, node, visited, curr)
            search(i - 1, j, node, visited, curr)
            visited.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                search(i, j, root, visited, "")

        return list(res)