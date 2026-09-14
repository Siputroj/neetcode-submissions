class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(temp, open, close):
            '''
            left open, right close
            if both right and open == n:
                return
            if open < 1 can only go open
            if open == n can only go close

            '''
            if open >= n and close >= n:
                res.append(temp)
                return
            
            if open < n:
                dfs(temp + '(', open + 1, close)
            
            if close < open:
                dfs(temp + ')', open, close + 1)

        dfs("", 0, 0)
        return res

            

            

            