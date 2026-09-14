class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def dfs(leftover):
            if not leftover:
                res.append(temp.copy())
                return

            for i in range(len(leftover)):
                temp.append(leftover[i])

                # will not be index out of bounds since its safe -- if list[a:b] where a is > len(list), 
                # then it will return []
                dfs(leftover[:i] + leftover[i + 1:])
                temp.pop()

        dfs(nums)
        return res