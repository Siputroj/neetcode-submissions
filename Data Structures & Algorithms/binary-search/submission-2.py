class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.iteration(nums, target)

    def iteration(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else: 
                start = mid + 1

        return -1

            
    def recursion(self, nums, target, start, end):
        pass 