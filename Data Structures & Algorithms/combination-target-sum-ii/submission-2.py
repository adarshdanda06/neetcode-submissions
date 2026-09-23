class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = set(), []

        def dfs(i, tot):
            if tot > target:
                return

            if tot == target:
                res.add(tuple(curr))
                return

            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dfs(j + 1, tot + candidates[j])
                curr.pop()
        
        dfs(0, 0)
        return [list(re) for re in res]