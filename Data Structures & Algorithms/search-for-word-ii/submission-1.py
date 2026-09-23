class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            curr = ""
            for i in range(len(word)):
                curr += word[i]
                if curr not in trie:
                    trie[curr] = False
            trie[curr] = True

        res = set()
        MCOLS, MROWS = len(board[0]), len(board)
        def search(i, j, curr, visited):
            if (i, j) in visited:
                return

            if i < 0 or i >= MROWS or j < 0 or j >= MCOLS:
                return

            curr += board[i][j]
            visited.add((i, j))
            if curr in trie:
                if trie[curr]:
                    res.add(curr)
  
                search(i, j - 1, curr, visited)
                search(i, j + 1, curr, visited)
                search(i - 1, j, curr, visited)
                search(i + 1, j, curr, visited)
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                search(i, j, "", visited)

        return list(res)