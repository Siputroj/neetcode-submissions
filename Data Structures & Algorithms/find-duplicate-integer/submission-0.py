class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if you know u have n + 1 integers, and range is between 1-n, then everythign will be unique, 1-n, and 1 will be extra
        table = {}
        for i in range(0, len(nums)):
            if nums[i] in table:
                return nums[i]

            table[nums[i]] = i