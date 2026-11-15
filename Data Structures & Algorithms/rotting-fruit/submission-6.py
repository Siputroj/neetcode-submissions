class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_fruits = 0
        rotten = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_fruits += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        def infect(row, col):
            nonlocal total_fruits
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 2
                total_fruits -= 1
                rotten.append((row, col))

        time = 0
        # Stop immediately once no fresh oranges remain
        while rotten and total_fruits > 0:
            time += 1
            for _ in range(len(rotten)):
                rot_r, rot_c = rotten.popleft()
                infect(rot_r + 1, rot_c)
                infect(rot_r, rot_c + 1)
                infect(rot_r - 1, rot_c)
                infect(rot_r, rot_c - 1)

        return time if total_fruits == 0 else -1
        