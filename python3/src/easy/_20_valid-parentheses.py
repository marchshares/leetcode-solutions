from typing import List


class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        for parenthesis in s:
            if parenthesis == '(' or parenthesis == '{' or parenthesis == '[':
                stack.append(parenthesis)
            else:
                if len(stack) == 0:
                    return False

                last_open_parenthesis = stack.pop()

                if parenthesis == ')' and last_open_parenthesis != '(':
                    return False

                if parenthesis == '}' and last_open_parenthesis != '{':
                    return False

                if parenthesis == ']' and last_open_parenthesis != '[':
                    return False

        return len(stack) == 0


test_cases = [
    {'s': "()", 'expected': True},
    {'s': "()[]{}", 'expected': True},
    {'s': "(]", 'expected': False},
    {'s': "([])", 'expected': True},
]

for idx, case in enumerate(test_cases, 0):
    s = case['s']
    expected = case['expected']

    res = Solution().isValid(s)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

