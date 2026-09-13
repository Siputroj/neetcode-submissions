class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            
            # Valid subset
            if sum(subset) == target:
                res.append(subset.copy())
                return

            # Not valid
            elif i >= len(nums) or sum(subset) > target:
                return 

            else:

                # I can reuse the same number again, so same index
                subset.append(nums[i])
                dfs(i)
                subset.pop()

                dfs(i+1)

        dfs(0)

        return res