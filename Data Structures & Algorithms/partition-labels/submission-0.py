class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #letter can appear in only one substring
        #xyxxyzbzbbisl

        #any overlap means they need to be in same substring
        #if last of prev greater than min of cur, they are in same substirng
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = [i, i]
            else:
                hash_map[s[i]][1] = i
        ans = []
        print(hash_map)
        cur_low = hash_map[s[0]][0]
        cur_end = hash_map[s[0]][1]
        k = list(hash_map.keys())
        for i in range(1, len(hash_map)):
            low = hash_map[k[i]][0]
            high = hash_map[k[i]][1]
             
            
            #group together
            if low < cur_end:
                if high > cur_end:
                    cur_end = high
                    
            else:
                ans.append(cur_end - cur_low + 1) 
                print(low, high)
                cur_low = low
                cur_end = high

        ans.append(cur_end - cur_low + 1)   
        return ans

