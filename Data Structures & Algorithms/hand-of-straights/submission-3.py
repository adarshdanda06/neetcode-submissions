class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hash_map = {}
        for num in hand:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        hash_list = sorted(list(hash_map.keys()))

        start = -1
        count = 0
        groups = 0
        i = 0
        print(hash_list)
        while groups < len(hand) / groupSize:
            while start == -1 and i < len(hash_list):
                if hash_map[hash_list[i]] != 0:
                    start = i
                    hash_map[hash_list[i]] -= 1
                else:
                    i += 1
            print(hash_list[start] + count)
            if start == -1:
                return False
            if count == 0:
                count += 1
            else:
                
                if hash_list[start] + count not in hash_map or hash_map[hash_list[start] + count] == 0:
                    return False
                else:
                    hash_map[hash_list[start] + count] -= 1
                    count += 1
                    
            
            if count == groupSize:
                groups += 1
                start = -1
                i = 0
                count = 0
                
        return True
            

        #make a hash_map
        
        