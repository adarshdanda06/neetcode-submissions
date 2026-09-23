class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
       
        #if something causes negative, start after that one
        start_ind = 0
        i = start_ind
        tot = 0
        count = 0
        while (count <= len(gas)):
            tot += gas[i] - cost[i]
            count += 1
            if tot < 0:
                start_ind = i + 1
                i = start_ind
                tot = 0
                count = 0
            else:
                i += 1
            start_ind %= len(gas)
            i %=  len(gas)            
        return start_ind

        