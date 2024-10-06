from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def func(left: int, right: int, s: str):
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                func(left+1, right, s + '(')

            if right < left:
                func(left, right+1, s + ')')

        func(0, 0, "")

        return res


test_cases = [
    {'n': 1, 'expected': ["()"]},
    {'n': 2, 'expected': ["(())", "()()"]},
    {'n': 3, 'expected': ["((()))","(()())","(())()","()(())","()()()"]},

]

for idx, case in enumerate(test_cases, 0):
    n = case['n']
    expected = case['expected']

    res = Solution().generateParenthesis(n)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

