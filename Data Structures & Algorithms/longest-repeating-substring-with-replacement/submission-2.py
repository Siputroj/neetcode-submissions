class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]]) 
            
            # while and if works here because the change in max values will at most change by 1, 
            # so only 1 step needed to fix
            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res