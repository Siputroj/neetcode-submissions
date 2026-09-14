class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # with duplicates you want to sort, so you know which have duplicates
        nums.sort()
        res = []
        temp = []

        def dfs(i):
            if i >= len(nums):
                res.append(temp.copy())
                return

            

            temp.append(nums[i])
            dfs(i + 1)
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            temp.pop()
            dfs(i + 1)

        dfs(0)
        return res