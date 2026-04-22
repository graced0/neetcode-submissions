class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            r, c = q.popleft()
            distance = grid[r][c] + 1
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                    q.append((nr, nc))
                    grid[nr][nc] = distance
