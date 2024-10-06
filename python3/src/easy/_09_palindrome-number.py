from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        if x % 10 == 0:
            return False

        x_reversed = 0

        while x > x_reversed:
            x_new = x // 10

            if x_new == x_reversed:
                return True

            x_mod = x % 10
            x_reversed = x_reversed * 10 + x_mod
            if x_new == x_reversed:
                return True

            x = x_new

        return False


test_cases = [
    {'x': 21120, 'expected': False},
    {'x': 121, 'expected': True},
    {'x': -121, 'expected': False},
    {'x': 10, 'expected': False},
    {'x': 1, 'expected': True},
]

for idx, case in enumerate(test_cases, 0):
    x = case['x']
    expected = case['expected']

    res = Solution().isPalindrome(x)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

