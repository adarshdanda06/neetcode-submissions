class KthLargest:
    # 7 6 4 10 8 9 1 
    # k = 5
    # then return 4

    # add k elem to a min heap
    # 9

    # maintain heap of size k
    # add takes in one, then we evict elem
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
