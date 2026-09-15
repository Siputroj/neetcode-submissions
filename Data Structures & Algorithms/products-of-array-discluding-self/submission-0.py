class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
                continue
            product *= num

        res = []
        if zero_counter > 0:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for i in range(len(nums)):
                res.append(product // nums[i])

        return res