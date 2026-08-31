class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            # while and if works here because the change in max values will at most change by 1, 
            # so only 1 step needed to fix
            while right - left + 1 - max(count.values()) > k:
                count[s[left]] = count.get(s[left]) - 1
                left += 1

            res = max(res, right - left + 1)

        return res

        