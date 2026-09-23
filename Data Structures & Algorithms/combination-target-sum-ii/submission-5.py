from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final = []
        def helper(i, arr, tot):
            if (tot == target):
                final.append(arr[:])
                return
            if (tot > target or i >= len(candidates)):
                return
            cur = candidates[i]
            arr.append(cur)
            helper(i + 1, arr, tot + cur)
            arr.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i + 1, arr, tot)
        helper(0, [], 0)
        return final
        
            

        

        