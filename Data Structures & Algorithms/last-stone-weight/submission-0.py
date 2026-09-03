class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            res = abs(stone_1 -  stone_2) * -1

            if res < 0:
                heapq.heappush(stones, res)
            
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0