# string is different than list, string is immutable so it makes a copy automatically and does not do in place operators
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # dict to map chars to digits
        translation = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        temp = ""
        if len(digits) < 1:
            return res

        def dfs(i):
            # telling python to not create a new local variable but used ones that has been made outside
            nonlocal temp
            if i >= len(digits):
                res.append(temp)
                return
            
            for value in translation.get(digits[i], []):
                temp += value
                dfs(i + 1)
                temp = temp[:-1]

        dfs(0)
        return res
        