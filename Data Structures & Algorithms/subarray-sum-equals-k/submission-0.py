class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        freq_map = {}

        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])

        total = 0
        for num in prefix:
            diff = num - k
            freq = freq_map.get(diff, 0)
            total += freq

            freq_map[num] = freq_map.get(num, 0) + 1

        return total
        