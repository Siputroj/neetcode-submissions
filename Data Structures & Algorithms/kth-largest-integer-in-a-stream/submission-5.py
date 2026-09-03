class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # what even list you get, heapify it, and make sure the length is k
        # this is so that the min value if the kth largest
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # push the new value into the heap and heappify
        heapq.heappush(self.min_heap, val)
        # maintain the length of min_heap = k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # the root is the kth largest value
        return self.min_heap[0]

        
