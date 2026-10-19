class Solution:
    def countSubstrings(self, s: str) -> int:
        # start with odd
        count = 0
        mid = 0
        l = r = mid
        for i in range(0, len(s)):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
            mid += 1
            l = r = mid
        
        # even
        if len(s) <= 1:
            return count
        
        m_l = 0
        m_r = 1
        l = m_l
        r = m_r
        for i in range(0, len(s)):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
            m_r += 1
            m_l += 1
            l = m_l
            r = m_r

        return count


            

        