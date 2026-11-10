class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque([])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for move in moves:
                    dr, dc = move
                    nr, nc = r + dr, c + dc 
                    

                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or (nr, nc) in visit:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    
                    visit.add((nr, nc))
                    q.append((nr,nc))
                    
                    grid[nr][nc] = dist
            
            dist += 1
