class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        left, right = 1, 2
        n = n - 2

        while n > 0:
            temp = right
            right = left + right
            left = temp
            n -= 1

        return right


