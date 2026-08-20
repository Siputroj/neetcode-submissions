class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max = 0
        curr_max = 0

        while start < end:
            min_height = min(heights[start], heights[end])
            curr_max = min_height * (end - start)

            if curr_max > max:
                max = curr_max

            if heights[start] <= heights[end]:
                start += 1
            
            elif heights[start] > heights[end]:
                end -= 1
        
        return max