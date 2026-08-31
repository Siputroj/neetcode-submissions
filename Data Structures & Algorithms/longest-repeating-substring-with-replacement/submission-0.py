class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            window = right - left + 1 - max(count.values())
            
            if window > k:
                count[s[left]] = count.get(s[left]) - 1
                left += 1

            res = max(res, right - left + 1)

        return res

        