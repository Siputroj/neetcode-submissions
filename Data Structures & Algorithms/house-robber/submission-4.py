class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # rob 1 is best rob until first index
        # rob 2 is best rob until second index
        rob_1, rob_2 = nums[0], max(nums[0], nums[1])
        
        if len(nums) == 2:
            return max(rob_1, rob_2)

        for i in range(2, len(nums)):
            temp = max(rob_1 + nums[i], rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return max(rob_1, rob_2)
        
