class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        
        wildCardMap = defaultdict(list)
        for i in range(len(beginWord)):
            fin = beginWord[0:i] + "*" + beginWord[i+1:]
            wildCardMap[fin].append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                fin = word[0:i] + "*" + word[i+1:]
                wildCardMap[fin].append(word)

        graph = defaultdict(set)
        for vals in wildCardMap.values():
            for i in range(len(vals)):
                for j in range(len(vals)):
                    if i != j:
                        graph[vals[i]].add(vals[j])


        print(graph)
        if len(graph[endWord]) == 0:
            return 0

        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            word, dist = q.pop()
            visited.add(word)

            for nbor in graph[word]:
                if nbor not in visited:
                    if nbor == endWord:
                        return dist + 1

                    q.append((nbor, dist + 1))

        return 0





            