class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # to calculate distance to a point = sqrt((x1 - x2)^2 + (y1 - y2)^2)

        heap = [(math.sqrt((x1) ** 2 + (y1) ** 2) * -1, [x1, y1]) for [x1, y1] in points]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        res = []

        for vals in heap:
            res.append(vals[1])

        return res