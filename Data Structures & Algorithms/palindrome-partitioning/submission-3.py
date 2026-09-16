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

        def dfs(remaining, path):
            if not remaining:
                res.append(path.copy())
                return
            
            for i in range(1, len(remaining) + 1):
                prefix = remaining[:i]
                if isPalindrome(prefix):
                    path.append(prefix)
                    dfs(remaining[i:], path)
                    path.pop()
            
        dfs(s, [])
        return res

        

            

        
        