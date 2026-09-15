class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        minimum = min(nums_set)
        nums_set.remove(minimum)
        res = 1
        temp = 1
        while nums_set:
            if minimum + 1 in nums_set:
                
                minimum = minimum + 1
                nums_set.remove(minimum)
                temp += 1
                res += 1
            else:
                if temp > res:
                    res = temp
                    temp = 1
                minimum = min(nums_set)
                nums_set.remove(minimum)

        return res

        