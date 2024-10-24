from typing import List
import inspect

from python3.src.utils import gen_test_case, gen_test_cases, get_test_method, run_test_cases


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        above_row = [1] * n

        for i_row in range(1, m):
            current_row = [1] * n
            for j_col in range(1, n):
                current_row[j_col] = current_row[j_col-1] + above_row[j_col]
            above_row = current_row

        return above_row[-1]


test_cases = gen_test_cases(
    """
    Input: m = 3, n = 7
    Output: 28
    """,

    """
    Input: m = 3, n = 2
    Output: 3
    """
)


run_test_cases(test_obj=Solution(), test_cases=test_cases)



