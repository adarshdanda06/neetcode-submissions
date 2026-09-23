class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        for key, value in count_map.items():
            arr[value].append(key)
        # [[], [], [1], [2], [3]]
        count = 0
        res = []
        for subarr in reversed(arr):
            for i in subarr:
                count += 1
                res.append(i)
                if count == k:
                    return res