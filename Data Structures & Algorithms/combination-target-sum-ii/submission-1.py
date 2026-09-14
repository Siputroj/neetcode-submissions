class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        # sort in ascending order for easier navigation
        candidates.sort()

        def dfs(i):
            if sum(temp) == target:
                if temp.copy not in res:
                    res.append(temp.copy())
                return
            
            if sum(temp) > target or i >= len(candidates):
                return

            temp.append(candidates[i])
            dfs(i + 1)
            
            temp.pop()

            # skip every duplicate 
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res