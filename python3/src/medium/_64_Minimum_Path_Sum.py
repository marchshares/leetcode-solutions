from typing import List
from math import trunc

class Solution:
    def rec_func(self, row, col, grid):
        s = grid[row][col]

        if col == 0 and row == 0:
            return s

        if col == 0:
            return s + self.rec_func(row - 1, col, grid)

        if row == 0:
            return s + self.rec_func(row, col - 1, grid)

        return s+min(self.rec_func(row - 1, col, grid), self.rec_func(row, col - 1, grid))

    def minPathSum_rec(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.rec_func(m-1, n-1, grid)

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for row in range(0, m):
            for col in range(0, n):
                if row == 0 and col == 0:
                    grid[row][col] = grid[row][col]
                elif row == 0 and col != 0:
                    grid[row][col] += grid[row][col-1]
                elif row != 0 and col == 0:
                    grid[row][col] += grid[row-1][col]
                elif row != 0 and col != 0:
                    grid[row][col] += min(grid[row][col-1], grid[row-1][col])

        return grid[m-1][n-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
res = Solution().minPathSum(grid)
assert res == 7, res

grid = [[1,2,3],[4,5,6]]
res = Solution().minPathSum(grid)
assert res == 12, res

