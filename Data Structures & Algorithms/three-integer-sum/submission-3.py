class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for i in range(len(nums)):
            target = 0 -nums[i]
            front = i + 1
            back = len(nums) - 1
            while front < back:
                if nums[front] + nums[back] == target:
                    res.add((nums[front], nums[back], nums[i]))
                    front += 1
                    back -= 1
                elif nums[front] + nums[back] < target:
                    front += 1
                elif nums[front] + nums[back] > target:
                    back -= 1

        return list(res)