class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # do a for loop to go through all the words
        # if the first word is found do a bfs
        def dfs(temp, x, y):
            if temp == word:
                return True
            
            dfs(temp + board[x][y], x, y)
            dfs(temp + board[x][y], x, y)
            dfs(temp + board[x][y], x, y)