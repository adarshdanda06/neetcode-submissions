class MedianFinder:

    # balanced heaps
    # min heap
    # max heap

    # ideal is len diff between both is <= 1

    # max_heap store 

    # 1 3 5 6 
    # we want the min heap to have elems geq to median
    # we want the max heap to have elems leq median


    # min heap stores -> 5 6 7
    # max heap stores -> 3 1

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        min_heap = self.min_heap
        max_heap = self.max_heap
        if len(min_heap) == 0 and len(max_heap) == 0:
            heapq.heappush(min_heap, num)
            return

        if len(max_heap) > 0 and num < -1 * max_heap[0]:
            heapq.heappush(max_heap, -1 * num)
        else:
            heapq.heappush(min_heap, num)

        
        if len(max_heap) - len(min_heap) > 1:
            top = -1 * heapq.heappop(max_heap)
            heapq.heappush(min_heap, top)
        elif len(min_heap) - len(max_heap) > 1:
            top = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1 * top)

        # len both 0, add to min heap
        # if val < top of max heap, add to max heap
        # if val > top of min heap, add to min heap


        # if len of max - len min > 1:
            # pop from max add to min

        # if len of min - len max > 1
            # pop from min add to max

    def findMedian(self) -> float:
        min_heap = self.min_heap
        max_heap = self.max_heap
        if len(min_heap) > len(max_heap):
            return min_heap[0]

        if len(max_heap) > len(min_heap):
            return -1 * max_heap[0]

        max_top = -1 * max_heap[0]
        min_top = min_heap[0]

        return (max_top + min_top) / 2
        