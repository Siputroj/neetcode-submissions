# brute force would be to do a for loop for all the digits and check all the characters
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # dict to map chars to digits
        translation = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        if len(digits) < 1:
            return res
            
        def dfs(i, string):
            if i >= len(digits):
                res.append(string)
                return
            
            for value in translation.get(digits[i], []):
                dfs(i + 1, string + value)

        dfs(0, "")
        return res
        