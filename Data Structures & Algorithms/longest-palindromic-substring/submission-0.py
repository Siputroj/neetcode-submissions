class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand outwards
        if len(s) == 1:
            return s
        max = ""

        for i in range(len(s)):
            l = i - 1
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            sub = s[i:j]
            r = j

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                   sub = s[l:r + 1]
                l -= 1
                r += 1

            if len(sub) > len(max):
                max = sub

        return max
 