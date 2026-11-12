class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        memo = {}
        
        def helper(power):
            if power == 1:
                return x
            
            first = power // 2
            second = power - first
            if power in memo:
               res = memo[power] 
            else:
                res = helper(first) * helper(second)
                memo[power] = res

            return res

        final_res = helper(abs(n))

        return final_res if n > 0 else 1/final_res

