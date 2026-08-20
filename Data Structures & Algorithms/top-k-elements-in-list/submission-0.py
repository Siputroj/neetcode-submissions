class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # initialize the array to size of nums + 1 because if len of nums is 4, 
        # max freq is 4 --> index of 4 therefore array needs to be of size 5
        freq = [[] for i in range(len(nums) + 1)]

        # loop through the nums array and get the freq of each number
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # store the dict in an array, where the index is the frequency of that number
        for num, count in counts.items():
            freq[count].append(num)

        # loop through the freq array from end to start
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                

        
        