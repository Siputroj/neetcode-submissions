class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left, right, mid
        # if left and mid > right:  left = mid
        # if left > mid and right: right = mid

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right -  left) // 2)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

