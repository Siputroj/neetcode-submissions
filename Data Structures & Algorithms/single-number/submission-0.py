class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        first = 0
        second = 1

        while second < len(nums) and nums[first] == nums[second]:
            first += 2
            second += 2

        if second >= len(nums):
            return nums[-1]
        else:
            return first



        