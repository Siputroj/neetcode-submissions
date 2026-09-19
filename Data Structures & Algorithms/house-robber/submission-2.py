class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0

        if len(nums) == 1:
            return nums[0]

        # add even 
        # add odd

        def helper(total, i):
            if i >= len(nums):
                return total
            total += nums[i]
            return max(helper(total, i + 2), helper(total, i + 3))

        return max(helper(0, 0), helper(0, 1))

        