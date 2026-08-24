class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = min(heights[left], heights(right)) * (right - left)
        left, right = 0, len(heights) - 1
        max_vol = 0
        while right > left:
            
            vol = min(heights[left], heights[right]) * (right - left)
            if vol > max_vol:
                max_vol = vol

            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return max_vol
