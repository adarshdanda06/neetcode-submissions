from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        seen = set()
        def helper(i, arr, tot):
            if (tot == target):
                sorted_tup = tuple(sorted(arr))
                if sorted_tup not in seen:
                    seen.add(sorted_tup)
                    final.append(arr[:])
                return
            if (i >= len(candidates)):
                return
            cur = candidates[i]
            arr.append(cur)
            helper(i + 1, arr, tot + cur)
            arr.pop()
            helper(i + 1, arr, tot)
        helper(0, [], 0)
        return final
        
            

        

        