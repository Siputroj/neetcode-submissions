class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # do a for loop to go through all the words
        # if the first word is found do a bfs
        def dfs(i, row, col, visited):
            
            if i == len(word):
                return True
            
            # check if still in board
            if (row >= len(board) or col >= len(board[0])) and (row < 0 or col < 0) :
                return False
            # check if visited
            if (row, col) in visited:
                return False
            
            visited.add((row, col))

            if board[row][col] != word[i]:
                return False
            else:
                return dfs(i + 1, row + 1, col, visited) or dfs(i + 1, row, col + 1, visited) or dfs(i + 1, row - 1, col, visited) or dfs(i + 1, row, col - 1, visited)

        res = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    res = dfs(0, row, col, set())
                if res:
                    return True

        return False