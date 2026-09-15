class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        even, odd = 0, 1 
        res_even, res_odd = 0, 0
        while odd  < len(nums) or even < len(nums):
            if even < len(nums):
                res_even += nums[even]
            
            if odd < len(nums):
                res_odd += nums[odd]

            even += 2
            odd += 2

        return max(res_even, res_odd)