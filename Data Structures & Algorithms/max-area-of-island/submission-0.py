class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        res = 0
        

        def dfs(start_r, start_c):
            q = collections.deque([(start_r, start_c)])
            visit.add((start_r, start_c))
            moves = [(1, 0), (0,1), (-1, 0), (0, -1)]
            islands = 1

            while q:
                r, c = q.popleft()
                for dr, dc in moves:
                    nr, nc = (r + dr, c + dc)
                    if (nr, nc) not in visit and (nr < len(grid) and nr >= 0) and nc < len(grid[0]) and nc >= 0 and grid[nr][nc] == 1:
                        islands += 1
                        q.append((nr, nc))
                        visit.add(
                        (nr, nc))

            return islands

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    islands = dfs(r,c)
                    res = islands if islands > res else res

        return res
                        
                