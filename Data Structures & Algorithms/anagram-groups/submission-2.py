class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for current in strs:
            current_list = [0] * 26
            for i in range(len(current)):
                current_list[ord(current[i]) - ord('a')] += 1
            freq_dict[tuple(current_list)].append(current)

        return list(freq_dict.values())