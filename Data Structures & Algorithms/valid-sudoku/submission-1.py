class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        box = defaultdict(set)
        row = [set() for _ in range(9)]

        
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue

                
                box_idx = ((r // 3), (c // 3))

                if (val in col[c] 
                or val in row[r] 
                or val in box[box_idx]):
                    return False

                col[c].add(val)
                row[r].add(val)
                box[box_idx].add(val)

        return True
                
                   


            
            