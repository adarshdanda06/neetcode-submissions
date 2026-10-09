class FreqStack:

    def __init__(self):
        self.ind = 0
        self.freqMap = {} # this stores the number of occurences
        self.heap = []

        # ()
        # max heap: (num of occurences, ind it should be in, value stored / pushed)


    def push(self, val: int) -> None:
        heap = self.heap
        freqMap = self.freqMap
        ind = self.ind

        occurenceCount = freqMap.get(val, 0) + 1

        heapItem = (-1 * occurenceCount, -1 * ind, val)
        heapq.heappush(heap, heapItem)

        freqMap[val] = occurenceCount
        self.ind += 1


    def pop(self) -> int:
        heap = self.heap
        freqMap = self.freqMap

        heapItem = heapq.heappop(heap)
        occurenceCount, _, val = heapItem
        
        occurenceCount *= -1
        freqMap[val] = occurenceCount - 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()