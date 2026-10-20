class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 0 means split
        # -ve means split, unless there s even amount
        res = max(nums)

        curMin, curMax = 1, 1

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            res = max(curMax, res)
        return res

            


        

