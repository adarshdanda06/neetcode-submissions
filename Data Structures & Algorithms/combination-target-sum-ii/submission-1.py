class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        curr = []

        def dfs(i, total):
            if total == target:
                res.add(tuple(curr))
            if i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                num = candidates[j]
                curr.append(num)
                dfs(j + 1, total + num)
                curr.pop()
            
        dfs(0, 0)
        return [list(current) for current in res]