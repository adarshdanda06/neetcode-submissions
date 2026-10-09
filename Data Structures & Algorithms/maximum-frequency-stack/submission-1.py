class FreqStack:

    def __init__(self):
        self.freqCount = {}
        self.stacks = []

    def push(self, val: int) -> None:
        freqMap = self.freqCount
        stacks = self.stacks

        freq = freqMap.get(val, 0) + 1

        if freq > len(stacks):
            stacks.append([])
        
        indToAppend = freq - 1
        stacks[indToAppend].append(val)

        freqMap[val] = freq


    def pop(self) -> int:
        stacks = self.stacks
        freqMap = self.freqCount

        val = stacks[-1].pop()
        
        if len(stacks[-1]) == 0:
            stacks.pop()    

        freqMap[val] -= 1
        return val





# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()