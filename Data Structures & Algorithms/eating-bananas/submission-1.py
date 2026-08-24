class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sum (x[i]/k) < 4, minimize k
        # upper bound for k is max(piles)and lower bound is 1 (1 banana per hour)

        upper = max(piles)
        lower = 1
        best_k = max(piles)

        while lower <= upper:
            mid = lower  + ((upper - lower) // 2)
            total_time = 0 
            for pile in piles:
                total_time = total_time + math.ceil(pile / mid)
            
            if total_time > h:
                lower = mid + 1
            elif total_time <= h:
                best_k = mid
                upper = mid - 1
        
        return best_k