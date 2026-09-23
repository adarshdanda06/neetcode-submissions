class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = set(), []

        def dfs(i, tot):
            if tot == target:
                res.add(tuple(curr))
                return
            if i >= len(candidates) or tot > target:
                return
            curr.append(candidates[i])
            dfs(i + 1, tot + candidates[i])
            curr.pop()

            dfs(i + 1, tot)
        
        dfs(0, 0)
        return [list(re) for re in res]