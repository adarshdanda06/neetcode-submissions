class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wildCardMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                fin = word[0:i] + "*" + word[i+1:]
                wildCardMap[fin].append(word)

        q = deque([beginWord])
        res = 1
        visited = set()

        while q:
            count = len(q)
            for j in range(count):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in wildCardMap[pattern]:
                        if w not in visited:
                            q.append(w)
                            visited.add(w)
            res += 1

        return 0





            