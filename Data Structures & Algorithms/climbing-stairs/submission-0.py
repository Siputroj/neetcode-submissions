class Solution:
    def climbStairs(self, n: int) -> int:
        # number of ways to get up:
        '''
        1 -> 1
        2 -> 2
        3 -> 3
        4 -> 5
        5 -> 8

        '''

        def helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2

            return helper(n - 1) + helper(n - 2)

        return helper(n)