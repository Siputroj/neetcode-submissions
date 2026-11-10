import collections
from typing import List


class Solution:

  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    res = 0

    def bfs(start_r: int, start_c: int):
      q = collections.deque([(start_r, start_c)])
      visit.add((start_r, start_c))

      directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

      while q:
        r, c = q.popleft()
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          # Check bounds, unvisited status, and land character
          if (
              0 <= nr < rows
              and 0 <= nc < cols
              and grid[nr][nc] == "1"
              and (nr, nc) not in visit
          ):
            visit.add((nr, nc))
            q.append((nr, nc))

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1" and (r, c) not in visit:
          bfs(r, c)
          res += 1

    return res