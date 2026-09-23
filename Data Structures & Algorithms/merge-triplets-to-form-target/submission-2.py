class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        first_set = set()
        second_set = set()
        third_set = set()
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                first_set.add(triplets[i][0])
                second_set.add(triplets[i][1])
                third_set.add(triplets[i][2])
        
        if target[0] not in first_set or target[1] not in second_set or target[2] not in third_set:
            return False
        return True