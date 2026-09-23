class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = [s[0]]
        res = []

        def branch(i):
            if i >= len(s):
                res.append(curr.copy())
                return

            curr.append(s[i])
            branch(i + 1)
            curr.pop()

            curr[-1] = curr[-1] + s[i]
            branch(i + 1)
            curr[-1] = curr[-1][:-1]

        branch(1)
        ans = []
        for word_list in res:
            add = True
            for word in word_list:
                if len(word) == 1:
                    continue
                
                for i in range(len(word)):
                    if word[i] != word[len(word) - 1 - i]:
                        add = False
            
            if add:
                ans.append(word_list)

        return ans
                
