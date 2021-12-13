from typing import List
from math import trunc

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(0, trunc(N/2)):
            for j in range(0, trunc((N - 1) / 2) + 1):
                print(f"{i},{j} -> {N-i-1}{j}")

                tmp = matrix[i][j]
                matrix[i][j] = matrix[N-j-1][i]
                matrix[N-j-1][i] = matrix[N-i-1][N-j-1]
                matrix[N-i-1][N-j-1] = matrix[j][N-i-1]
                matrix[j][N-i-1] = tmp




matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
assert matrix == [[7,4,1],[8,5,2],[9,6,3]], matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

matrix = [[1]]
Solution().rotate(matrix)
assert matrix == [[1]]

matrix = [[1,2],[3,4]]
Solution().rotate(matrix)
assert matrix == [[3,1],[4,2]]




