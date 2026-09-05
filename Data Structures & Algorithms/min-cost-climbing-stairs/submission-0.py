class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost to finish is comparing cost to get to the second last and the last step
        self.memo = {}

        def helper(cost, k):

            if k == 0:
                return cost[0]
            if k == 1:
                return cost[1]

            if self.memo.get(k - 1, 0) == 0:
                self.memo[k - 1] = helper(cost, k - 1)
            
            if self.memo.get(k - 2, 0) == 0:
                self.memo[k - 2] = helper(cost, k - 2)
            
            cost_a = self.memo[k - 1] 
                
            cost_b = self.memo[k - 2] 

            curr_cost = cost[k] if k < len(cost) else 0


            return min(cost_a, cost_b) + curr_cost

            

        return helper(cost, len(cost))
        