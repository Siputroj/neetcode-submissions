class Solution:
    def numDecodings(self, s: str) -> int:
        table = {"1": "A", "2": "B", "3": "C", "4": "D", "5":"E", "6": "F", "7":"G", "8":"H", "9":"I", "10":"J", "11":"K", "12":"L", "13":"M", "14":"N", "15":"O", "16":"P", "17":"Q", "18":"R", "19":"S", "20":"T", "21":"U", "22":"V", "23":"W", "24":"X", "25":"Y", "26":"Z"}
        memo = {}
        def helper(start):
            if start == len(s):
                return 1

            if start in memo:
                return memo[start]

            count = 0
            
            if start + 1 <= len(s) and s[start : start + 1] in table:
                count += helper(start + 1)
            
            if start + 2 <= len(s) and s[start : start + 2] in table:
                count += helper(start + 2)

            memo[start] = count
            return count

        return helper(0)
         
