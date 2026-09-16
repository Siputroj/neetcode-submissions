class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # function to check if palindrome
        def isPalindrome(word) -> bool:
            if len(word) == 0:
                return False

            if len(word) == 1:
                return True
            l, r = 0, len(word) - 1
            
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(substr):
            if len(substr) == 1:
                temp.append(substr)
                return

            if isPalindrome(substr):
                temp.append(substr)
                res.append(temp.copy())
                temp.pop()
            
            # go right -- WRONG cannot split like this, will miss middle palindrome "abbab" --> miss "a, bb, a, b" because we only check the first first char of substring
            dfs(substr[0])

            # go left
            dfs(substr[1:])

        # do for loop and then a dfs
        for i in range(len(s)):
            temp = []
            if isPalindrome(s[:i + 1]):
                temp.append(s[:i + 1])

                if len(s[i + 1:]) > 0:
                # run the dfs for s[i + 1:]
                    dfs(s[i + 1:])
                res.append(temp.copy())

        return res

        

            

        
        