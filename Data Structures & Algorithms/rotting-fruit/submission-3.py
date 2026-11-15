class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # stack and loop and time counter
        # at the end, check if there are any fruit remaining
        rows, cols = len(grid), len(grid[0])
        total_fruits = 0
        rotten = collections.deque([])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_fruits += 1
                if grid[r][c] == 2:
                    rotten.append((r, c))
                    visited.add((r, c))
        
        if len(rotten) < 1:
            if total_fruits >= 1:
                return -1
            else:
                return 0

        def infect(row, col):
            nonlocal total_fruits
            if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == 1:
                print(f"infected:{row}, {col}")
                grid[row][col] = 2
                total_fruits -= 1
                rotten.append((row, col))
            visited.add((row, col))


        time = 0
        while rotten:
            time += 1
            print(f"Time {time} ===================")
            
            for i in range(len(rotten)):
                rot_r, rot_c = rotten.popleft()
                infect(rot_r + 1, rot_c)
                infect(rot_r, rot_c + 1)
                infect(rot_r - 1, rot_c)
                infect(rot_r, rot_c - 1)

        return time - 1 if total_fruits == 0 else -1