class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums_set = set(nums)
        rand = nums_set.pop()
        rand_front = rand_back = rand
        res = 1
        temp = 1
        while nums_set:
            print(temp)
            if rand_front + 1 in nums_set:
                rand_front += 1
                nums_set.remove(rand_front)
                temp += 1

            elif rand_back - 1 in nums_set:
                rand_back -= 1
                nums_set.remove(rand_back)
                temp += 1

            else:
                if temp > res:
                    res = temp
                temp = 1
                rand = rand_back = rand_front = nums_set.pop()

        res = max(res, temp)

        return res

        