class Solution:
    def isIsland(self, r,c, grid, nr, nc):
            if r >= 0 and r < nr and \
                c >= 0 and c < nc and \
                grid[r][c] is "1":
                grid[r][c] = '0'
                self.isIsland(r+1, c, grid, nr, nc)
                self.isIsland(r-1, c, grid, nr, nc)
                self.isIsland(r, c+1, grid, nr, nc)
                self.isIsland(r, c-1, grid, nr, nc)
    def numIslands(self, grid):
        nr = len(grid)
        nc = len(grid[0])
        cnt = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    cnt += 1
                    self.isIsland(r,c, grid, nr, nc)
            
        return cnt
