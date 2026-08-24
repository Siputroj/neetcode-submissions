class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left, right, mid
        # if left and mid > right:  left = mid
        # if left > mid and right: right = mid

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[left] > nums[right]:
                if nums[right] > nums[mid]:
                    right = mid 
                elif nums[right] < nums[mid]:
                    left = mid + 1
            else:
                return nums[left]
