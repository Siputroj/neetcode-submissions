class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sort(nums)
        res = []

        for num in nums:
            front = 0
            back = len(nums) - 1
            temp_res = []
            while back > front:

                if nums[front] + nums[back] < -num:
                    back -= 1

                if nums[front] + nums[back] > -nums:
                    front += 1

                if nums[front] + nums[back] == -nums:
                    temp_res.append(front)
                    temp_res.append(front)
                    temp_res.append(front)
                    
                    