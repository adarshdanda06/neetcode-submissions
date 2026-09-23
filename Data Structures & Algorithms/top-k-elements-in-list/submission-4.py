from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ans = []
        for i in nums:
            count[i] += 1
        [1, 2, 2, 3, 3, 3]

        
        buckets = [[] for i in range(len(nums))]
        for i in count:
            buckets[count[i] - 1].append(i)
        
        
        print(buckets)
        count = 0
        i = len(buckets) - 1
        while count < k and i >= 0:
            if len(buckets[i]) > 0:
                count += len(buckets[i])
                ans.append(buckets[i])
            i -= 1
        final_ans = []
        for i in ans:
            for j in i:
                final_ans.append(j)
        return final_ans

