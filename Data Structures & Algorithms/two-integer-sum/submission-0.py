class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key target - element, value is index
        res = {}

        for i in range(len(nums)):

            if nums[i] in res:
                return [res.get(nums[i]), i]
            
            res[target - nums[i]] = res.get(target - nums[i], i)
            
