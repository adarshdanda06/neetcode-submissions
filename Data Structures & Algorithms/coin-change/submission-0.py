class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        elems = {}
        for i in range(amount + 1):
            elems[i] = float('inf')
        elems[0] = 0
        coins.sort()

        for i in range(len(coins) -1, -1, -1):
            ind = 0
            while ind < len(elems):
                if ind + coins[i] in elems:
                    elems[ind + coins[i]] = min(elems[ind] + 1, elems[ind + coins[i]])
                ind += 1
        
        return elems[amount] if elems[amount] != float('inf') else -1

            