class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left)// 2)

            if target < nums[mid]:
                if target < nums[left]:
                    left = mid + 1
                else:
                    right = mid

            elif target > nums[mid]:
                if target > nums[right]:
                    right = mid
                else:
                    left = mid + 1
            else:
                return mid
        
        return -1

                



        