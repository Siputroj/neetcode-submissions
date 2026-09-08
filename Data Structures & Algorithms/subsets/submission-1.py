from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for n in nums:
            stage = []

            for s in output:
                new_s = s.copy()
                new_s.append(n)
                stage.append(new_s)

            output.extend(stage)

        return output
