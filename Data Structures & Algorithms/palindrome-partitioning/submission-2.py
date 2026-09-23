class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #in every list all characters are included, just in different partitions
        #every s has at least one pos, which just one char in each partition
        #whether we want to include the s[i] in cur partition or next partition
        ans = []
        def backtrack(i, cur):
            if (i == len(s)):
                ans.append(cur[:])
                return
            for j in range(i + 1, len(s) + 1):
                cur_str = s[i:j]
                if is_palindrome(cur_str):
                    cur.append(cur_str)
                    backtrack(j, cur)
                    cur.pop()
        def is_palindrome(string):
            return string == string[::-1]
        backtrack(0, [])
        return ans