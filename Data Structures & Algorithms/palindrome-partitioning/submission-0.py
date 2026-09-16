class Solution:
    def partition(self, s: str) -> List[List[str]]:

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

        # do for loop and then a dfs
        for i in range(len(s)):
            temp = []
            if isPalindrome(s[:i + 1]):
                temp.append(s[:i + 1])
                # run the dfs for s[i + 1:]
                dfs(s[i + 1:])
                res.append(temp)

        def dfs(substr):

            if len(substr) == 1:
                temp.append(substr)
                return

            
            # go right    
            dfs(substr[0])

            if isPalindrome(substr[1:]):
                temp.append(substr)
                res.append(temp)
                temp.pop()

            # go left
            dfs(substr[1:])

            

        
        