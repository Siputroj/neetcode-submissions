class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount, count): # return num of coins
            if amount < 0:
                return

            if amount in memo:
                if memo[amount] < count:
                    return

            memo[amount] = count

            for coin in coins:
                helper(amount - coin, count + 1)

        helper(amount, 0)
        return memo.get(0, -1)